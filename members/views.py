from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, EditProfile

# Members views are here.


def login_user(request):
    if request.method == "POST":
        print("request")

        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Login Failed! Please, Try Again."))	
            return redirect('booking')	

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, ("You are logged out."))
    return redirect('index')

def register_user(request):

    register_to_book = request.GET.get('rtb', "false") == 'true'

    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, ('Registration Successful!'))
                if register_to_book:
                    return redirect('/booking?rtb=true')
                else:
                    return redirect('/booking')
            else:
                return redirect('index')
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {'form': form, 'register_to_book': register_to_book,})

    
def user_profile(request):
    
    is_edit = request.GET.get('edit', "false") == 'true'
    
    is_delete = request.GET.get('delete', "false") == 'true'

    user = request.user
    delete_pwd = ''

    try:
        delete_pwd = request.POST['pwd_for_delete']
    except:
        pass
    
    if delete_pwd != '':
        try:
            user = authenticate(request, username=request.user.email, password=delete_pwd)

            if user is not None:
                logout(request)
                user.delete()
                messages.success(request, "The user is deleted")
                return redirect('index')
            else:
                messages.success(request, ("Delete Failed! Please, Try Again."))	
                return redirect('index')
        except:
            messages.success(request, ("Delete Failed!"))

        return redirect('user_profile')

    form = EditProfile(request.POST or None, instance=user)
    
    if request.method == "POST" and form.is_valid():
        form.save()
        
        return redirect('user_profile')

    return render(request, 'user_profile.html', {'form': form, 'is_edit': is_edit, 'is_delete': is_delete,})




'''
    except:
        # do nothing

    if delete_pwd != None:
        print('DELETE')
        return redirect('user_profile')


'''
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
            return redirect('booking')	

    else:
        return render(request, 'authenticate/login.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')

def register_user(request):

    register_to_book = request.GET.get('rtb', "false") == 'true'

    form_errors = []
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if register_to_book:
                    return redirect('/booking?rtb=true')
                else:
                    return redirect('/booking')
            else:
                return redirect('index')
        else:
            password1 = form.data['password1']
            password2 = form.data['password2']
            email = form.data['email']
            for msg in form.errors.as_data():
                if msg == 'email':
                    form_errors.append(f"Declared email: {email} is not valid")
                if msg == 'password2' and password1 == password2:
                    form_errors.append("The selected password is not strong enough")
                elif msg == 'password2' and password1 != password2:
                    form_errors.append("The entered passwords do not match")
        
    else:
        form = RegisterUserForm()

    return render(request, 'authenticate/register_user.html', {'form': form, 'form_errors': form_errors, 'register_to_book': register_to_book,})

    
def user_profile(request):
    
    is_edit = request.GET.get('edit', "false") == 'true'

    is_cancel = request.GET.get('cancel', "false") == 'true'

    is_delete = request.GET.get('delete', "false") == 'true'
    
    user = request.user
    delete_pwd = ''

    user_error_msg = []

    try:
        delete_pwd = request.POST['pwd_for_delete']
    except:
        pass
    
    if delete_pwd != '':
        is_delete = True
        try:
            user = authenticate(request, username=request.user.email, password=delete_pwd)

            if user is not None:
                logout(request)
                user.delete()
                return redirect('index')
            else:
                user_error_msg.append("Delete Failed! Please, Try Again.")
        except:
            return redirect('index')

    asdkl = request.POST or None

    if is_delete:
        form = EditProfile(instance=request.user)
    else:
        form = EditProfile(request.POST or None, instance=request.user)


    if not is_edit:
        form.fields['first_name'].widget.attrs["disabled"] = 'true'
        form.fields['last_name'].widget.attrs["disabled"] = 'true'
        form.fields['email'].widget.attrs["disabled"] = 'true'
        form.fields['address'].widget.attrs["disabled"] = 'true'

    if not is_delete:
        if request.method == "POST" and form.is_valid() and not is_cancel:
            form.save()
        
            return redirect('user_profile')

    return render(request, 'user_profile.html', {'form': form, 'is_edit': is_edit, 'is_delete': is_delete, 'user_error_msg': user_error_msg})




'''
    except:
        # do nothing

    if delete_pwd != None:
        print('DELETE')
        return redirect('user_profile')


'''
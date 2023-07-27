from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


def login_user(request):
    if request.method == "POST":
        print("request")

        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.success(request, ("Login Failed! Please, Try Again."))	
            return redirect('login')	

    else:
        return render(request, 'authenticate/login.html', {})

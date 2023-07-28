from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView
from .models import Testimonial
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.


#def index(request):
#    return render(request, 'index.html')

def testimonial(request):
    all_testimonials = Testimonial.objects.filter(status='1')
    return render(request, 'testimonials.html', { 'all_testimonials': all_testimonials})

#def login_user(request):
#    return render(request, 'login.html', {})

# def home(request):
#    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html', {})

def about(request):
    return render(request, 'about.html', {})

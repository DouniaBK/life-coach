from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import ListView
from .models import Testimonial
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def index(request):
    all_testimonials = Testimonial.objects.filter(status='1')
    return render(request, 'index.html', {'all_testimonials': all_testimonials})  # noqa


def services(request):
    return render(request, 'services.html', {})


def resources(request):
    return render(request, 'resources.html', {})


def error_404(request, exception):
    return render(request, 'errors.html', {
            'header': "Ooops...",
            'text': "We are sorry, but we could not find the page you are looking for."  # noqa
        })


def error_500(request, *args, **argv):
    return render(request, 'errors.html', {
            'header': "Ooops...",
            'text': "We are sorry, this should not happen but we just encountered an error."   # noqa
        })


def error_403(request, exception):
    return render(request, 'errors.html', {
            'header': "You shall not enter!",
            'text': "I have spoken"
        })


def error_400(request, exception):
    return render(request, 'errors.html', {
            'text': "This did not work. There seems to be a communication error."   # noqa
        })

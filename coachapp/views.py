from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView
from .models import Testimonial


# Create your views here.


#def index(request):
#    return render(request, 'index.html')

def testimonial(request):
    all_testimonials = Testimonial.objects.filter(status='1')
    return render(request, 'testimonials.html', { 'all_testimonials': all_testimonials})


# def home(request):
#    return render(request, 'index.html')

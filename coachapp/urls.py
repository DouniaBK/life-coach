from . import views
from django.urls import path
#from .views import TestimonialSectionView


urlpatterns = [
   path('', views.testimonial),
   #path('index', views.index)
]

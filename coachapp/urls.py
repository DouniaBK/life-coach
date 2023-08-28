from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('resources', views.resources, name='resources'),
   path('services', views.services, name='services'),
   path('index', views.index, name="index"),
   path('', views.index, name="index"),
]

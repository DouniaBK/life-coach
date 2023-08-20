from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
   #path('index', views.testimonial),
   path('resources', views.resources, name='resources'),
   path('services', views.services, name='services'),
   path('index', views.index, name="index"),
   path('', views.index, name="index"),
]

#path('', views.login_user),
#path('login_user', views.login_user, name='login'),
#path('index', views.index)
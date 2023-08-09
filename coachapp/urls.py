from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.testimonial),
   path('about', views.about, name='about'),
   path('services', views.about, name='services'),
   path('index', views.index, name="index"),
]

#path('', views.login_user),
#path('login_user', views.login_user, name='login'),
#path('index', views.index)
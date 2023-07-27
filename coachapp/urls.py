from . import views
from django.urls import path
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.testimonial),
]

#path('', views.login_user),
#path('login_user', views.login_user, name='login'),
#path('index', views.index)
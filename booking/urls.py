from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.booking, name='booking'),
   path('cancel_session', views.cancel_session, name="cancel_session"),
]
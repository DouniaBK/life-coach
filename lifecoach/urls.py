"""lifecoach URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import handler403, handler404, handler400, handler500
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('coachapp.urls'), name="coachapp-urls"),
    path('members/', include('django.contrib.auth.urls')),
    path('members/', include('members.urls')),
    path('booking/', include('booking.urls')),
]

handler400 = 'coachapp.views.error_400'
handler403 = 'coachapp.views.error_403'
handler404 = 'coachapp.views.error_404'
handler500 = 'coachapp.views.error_500'

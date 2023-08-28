from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from .managers import CustomUserManager
from django.conf import settings
from django.utils import timezone


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))


class CustomUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=50, default='Client')
    last_name = models.CharField(max_length=100, default='Client')
    address = models.CharField(max_length=400, default='Address')
    email = models.EmailField(("Email Address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class Testimonial(models.Model):
    name = models.CharField(max_length=80)
    body = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-name"]

    def __str__(self):
        return f'{self.name}'

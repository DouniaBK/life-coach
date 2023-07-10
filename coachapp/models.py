from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User
from django.utils import timezone
from .managers import CustomUserManager
from django.conf import settings


# Create your models here.

STATUS = ((0, "Draft"), (1, "Published"))
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(("Email Address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class testimonial(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()  # perhpas needs to be deleted 
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f'Testimony {self.body} by {self.name}'

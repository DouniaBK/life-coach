from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, testimonial
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = testimonial
        fields = ("body",)

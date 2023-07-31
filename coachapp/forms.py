from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, Testimonial
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("email", 'last_name', 'first_name')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ("email",)


class TestimonyForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ("body",)


class CustomAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    
    class Meta:
        model = CustomUser
        fields = ('email', 'last_name', 'first_name', 'password1', 'password2')

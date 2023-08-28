from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from coachapp.models import CustomUser


# Credit to John Atler from Codemy.com
class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=400)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address', 'password1', 'password2')   # noqa


class EditProfile(forms.ModelForm):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=100)
    address = forms.CharField(max_length=400)
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'address')

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }

from .widget import DateTimePickerInput
from django import forms
from .models import CoachingSession
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime   # noqa


COACHING_SERVICES_CHOICES = (
    ("Freedom and Thrive", "Freedom and Thrive"),
    ("Ignite Your Potential", "Ignite Your Potential"),
    ("Unleash Your Extraordinary Life", "Unleash Your Extraordinary Life"),
    ("Breakthrough to Freedom", "Breakthrough to Freedom"),
    )


class CoachingSessionInputForm(forms.ModelForm):
    service = forms.ChoiceField(choices=COACHING_SERVICES_CHOICES)
    time = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model = CoachingSession
        fields = ('user', "service", 'time')
        labels = {
            'user': 'Email',
            'service': 'Coaching Service',
            'time': 'Appointment',
        }
        widgets = {
            "time": AdminSplitDateTime(),
        }


class CoachingSessionInputFormFrontEnd(forms.ModelForm):
    service = forms.ChoiceField(choices=COACHING_SERVICES_CHOICES)
    time = forms.SplitDateTimeField(label='', widget=AdminSplitDateTime())

    class Meta:
        model = CoachingSession
        fields = ("service", 'time')
        labels = {
            'service': 'Coaching Service',
            'time': 'Appointment',
        }
        widgets = {
        }

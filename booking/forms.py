from .widget import DateTimePickerInput
from django import forms
from .models import Appointment

class AppointmentInputForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs=dict(type='date')))
    time = forms.DateField(widget=forms.DateInput(attrs=dict(type='time')))

    class Meta:
        model = Appointment
        fields = ('services', 'time')

from django import forms


class DateTimePickerInput(forms.DateTimeInput):
    input_type = 'datetime'
    input_formats = ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']
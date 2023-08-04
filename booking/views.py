from django.shortcuts import render, redirect
from datetime import datetime, timezone, timedelta
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .forms import CoachingSessionInputFormFrontEnd
from django.contrib import messages

# Create your views here.

def booking(request):
    
    offset_param = int(request.GET.get('offset', "0"))

    offset_weeks = timedelta(weeks=offset_param)

    # Get todays date and weekday
    t_current = datetime.now() + offset_weeks
    
    # get day of week as an integer
    weekday = t_current.weekday()

    days_of_the_week = {}
    for i in range(0-weekday, 7-weekday):
        t_day = t_current + timedelta(days=i)
        days_of_the_week[t_day.weekday()] = t_day.strftime("%m/%d/%Y")

    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = CoachingSessionInputFormFrontEnd(request.POST)
        # check whether it's valid:
        if form.is_valid():
            your_object = form.save(commit=False)
            your_object.user = request.user
            your_object.save()
            # process the data in form.cleaned_data as required
            service = form.cleaned_data['service']
            time = form.cleaned_data['time']
            messages.success(request, ('Your appointment has been booked.'))
            # redirect to a new URL:
        else:
            print("Error", form.errors)
        
    # if a GET (or any other method) we'll create a blank form
    form = CoachingSessionInputFormFrontEnd()
    return render(request, 'booking.html', {'form': form, 'weekdays': days_of_the_week, 'currentWeekOffset': offset_param})
from django.shortcuts import render
from datetime import datetime, timezone
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .forms import AppointmentInputForm

# Create your views here.


def booking(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AppointmentInputForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect("/thanks/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppointmentInputForm()

    return render(request, 'booking.html', {'form': form})



"""
    local = datetime.now()
    time_utc = datetime.utcnow()
    
    form = null
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = AppointmentInputForm(request.POST)

    local_conv = local.strftime("%m/%d/%Y, %H:%M:%S")
    time_utc_conv = time_utc.strftime("%m/%d/%Y, %H:%M:%S")
    dt_now_conv = time_utc.strftime("%m/%d/%Y, %H:%M:%S")

    today_to_utc_conv = local.utcnow().strftime("%m/%d/%Y, %H:%M:%S")

    date = 1
    weekdays = valid

def validWeekday(days):
    #Loop days you want in the next 21 days:
    today = datetime.now()
    weekdays = []
    for i in range (0, days):
        x = today + timedelta(days=i)
        y = x.strftime('%A')
        if y == 'Monday' or y == 'Saturday' or y == 'Wednesday':
            weekdays.append(x.strftime('%Y-%m-%d'))
    return weekdays"""
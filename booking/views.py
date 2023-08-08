from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from datetime import datetime, timezone, timedelta
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .forms import CoachingSessionInputFormFrontEnd
from django.contrib import messages
from .models import CoachingSession

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

    # Check in database for existing sessions during that week
    start_dt = datetime(2023, 8, 7)
    end_dt = datetime(2023, 8, 12)
    all_sessions = CoachingSession.objects.filter(time__gte=start_dt, time__lt=end_dt)

    sessions_of_the_week = {}
    for d in days_of_the_week:
        date_of_that_day = days_of_the_week[d]
        date_time_object_lower = datetime.strptime(date_of_that_day, "%m/%d/%Y")
        date_time_object_upper = date_time_object_lower + timedelta(days=1)
        days_sessions = all_sessions.filter(time__gte=date_time_object_lower, time__lte=date_time_object_upper)

        sessions_of_the_week[d] = []
        for s in days_sessions:
            sessions_time_hours = s.time.strftime("%H")
            sessions_of_the_week[d].append(sessions_time_hours)


    # Get all appointments of the user
   
    all_user_sessions_templ = []
    all_user_sessions = CoachingSession.objects.filter(user=request.user)
    for us in all_user_sessions:
        info = {}
        info["id"] =us.id
        info["time"] = us.time.strftime("%m/%d/%Y at %H:%M")

        all_user_sessions_templ.append(info)




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
            return HttpResponseRedirect("/booking")
        else:
            print("Error", form.errors)
        
    # if a GET (or any other method) we'll create a blank form
    form = CoachingSessionInputFormFrontEnd()
    return render(request, 'booking.html', {'form': form, 'weekdays': days_of_the_week, 'currentWeekOffset': offset_param, 'weeksSessions': sessions_of_the_week, 'allUserSessions': all_user_sessions_templ})


    
def cancel_session(request):
    # this cancels
    id = int(request.GET.get('id', "-1"))
    booked_session = get_object_or_404(CoachingSession, id=id) 
    if request.method == "GET":
        booked_session.delete()
        return HttpResponseRedirect("/booking")
    return render(request, "booking.html", context)
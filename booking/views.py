from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect   # noqa
from datetime import datetime, timezone, timedelta
from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .forms import CoachingSessionInputFormFrontEnd
from django.contrib import messages
from .models import CoachingSession
import json


# Returns the days of the week for a specific day
def getDaysOfWeekForDay(t_current):
    # Get day of week as an integer
    weekday = t_current.weekday()

    # Iterate over the days of the week and write them to the output
    days_of_the_week = {}
    for i in range(0-weekday, 7-weekday):
        t_day = t_current + timedelta(days=i)
        days_of_the_week[t_day.weekday()] = t_day.strftime("%m/%d/%Y")

    # Returns days of the week and weekday as an int
    return days_of_the_week, weekday


# Sort all_sessions by the day they occur
def sortSessionsByDay(all_sessions, days_of_the_week, user):
    sessions_of_the_week = {}
    # Iterate over all weekdays
    for d in days_of_the_week:
        # Filter the sessions that occur on the specific day
        date_of_that_day = days_of_the_week[d]
        date_time_object_lower = datetime.strptime(date_of_that_day, "%m/%d/%Y")  # noqa
        date_time_object_upper = date_time_object_lower + timedelta(days=1)
        days_sessions = all_sessions.filter(time__gte=date_time_object_lower, time__lte=date_time_object_upper)  # noqa

        # Format the time for the template and add 'me' if the session belongs to the current user # noqa
        sessions_of_the_week[d] = []
        for s in days_sessions:
            sessions_time_hours = s.time.strftime("%H")
            isme = s.user == user
            if isme:
                sessions_time_hours = sessions_time_hours + 'me'
            sessions_of_the_week[d].append(sessions_time_hours)
    return sessions_of_the_week


# Extract the week offset from the request, return 0 if not defined
def getOffsetFromRequest(request):
    offset_param = int(request.GET.get('offset', "0"))
    # In case a negative value is given, set back to zero
    # (protection against manual URL manipulation)
    if offset_param < 0:
        offset_param = 0
    return offset_param


# Booking view
# This view acts as middleware for the calendar, thus assembling all
# necessary information for viewing the calendar and handling session booking and cancelation. # noqa
def booking(request):
    try:
        # Special variable to indicate whether the booking is done in the context of the new registration # noqa
        register_to_book = request.GET.get('rtb', "false") == 'true'
        # Special variable to indicate whether the register and booking workflow was successful # noqa
        success = False
        if register_to_book:
            success = request.GET.get('success', "false") == 'true'

        # Min. hour to show in the calendar
        h_min = 8
        # Max. hour to show in the calendar
        h_max = 21

        # Week offset from current week
        offset_param = getOffsetFromRequest(request)
        offset_weeks = timedelta(weeks=offset_param)

        # Get todays date and weekday
        t_current = datetime.now() + offset_weeks

        # The all days of the current week and current weekday as int
        days_of_the_week, weekday = getDaysOfWeekForDay(t_current)

        # Check in database for existing sessions during that week
        start_dt = t_current.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=(0-weekday))   # noqa
        end_dt = start_dt + timedelta(days=7)
        all_sessions = CoachingSession.objects.filter(time__gte=start_dt, time__lt=end_dt)  # noqa

        sessions_of_the_week = sortSessionsByDay(all_sessions, days_of_the_week, request.user)   # noqa

        # Fill in all sessions in the past
        #  (grey out past days sessions in scheduler)
        week_now = int(datetime.now().strftime("%V"))
        week_current = int(t_current.strftime("%V"))
        if week_current == week_now:
            for d in days_of_the_week:
                if d <= weekday:
                    for i in range(h_min, h_max):
                        if not str(i) in sessions_of_the_week[d] and not (str(i) + "me") in sessions_of_the_week[d]:   # noqa
                            sessions_of_the_week[d].append(str(i))

        # Get all appointments of the user
        all_user_sessions_templ = []
        all_user_sessions = CoachingSession.objects.filter(user=request.user)
        for us in all_user_sessions:
            info = {}
            info["id"] = us.id
            info["service"] = us.service
            info["time"] = us.time.strftime("%m/%d/%Y at %H:%M")

            all_user_sessions_templ.append(info)

        # Assemble which hours need to be shown in the calendar
        hours_vec = []
        for i in range(h_min, h_max):
            hours_vec.append(str(i))

        # if this is a POST request, handle saving the session
        if request.method == "POST":
            # create a form instance and populate it with
            #  data from the request:
            form = CoachingSessionInputFormFrontEnd(request.POST)
            # check whether the form is valid:
            if form.is_valid():
                session_object = form.save(commit=False)
                session_object.user = request.user
                session_object.save()
                # process the data in form.cleaned_data as required
                service = form.cleaned_data['service']
                time = form.cleaned_data['time']
                # redirect to a new URL:
                if register_to_book:
                    return HttpResponseRedirect("/booking?rtb=true&success=true")  # noqa
                else:
                    return HttpResponseRedirect("/booking?offset=" + str(offset_param))   # noqa
            else:
                print("Error", form.errors)

        # if a GET (or any other method) we'll create a blank form
        form = CoachingSessionInputFormFrontEnd()
        return render(request,  'booking/booking.html', {'form': form,   # noqa
                                'weekdays': days_of_the_week,   # noqa
                                'currentWeekOffset': offset_param,   # noqa
                                'weeksSessions': sessions_of_the_week,   # noqa
                                'allUserSessions': all_user_sessions_templ,   # noqa
                                'scheduleHours': hours_vec,  # noqa
                                'isThisWeek': week_current == week_now,  # noqa
                                'register_to_book': register_to_book,  # noqa
                                'register_book_success': success,  # noqa
                                'scheduleHours_json': json.dumps(hours_vec), })  # noqa
    except Exception as e:
        print(str(e), e.args)
        return HttpResponseRedirect("")


def cancel_session(request):
    # this cancels
    offset_param = getOffsetFromRequest(request)

    id = int(request.GET.get('id', "-1"))
    booked_session = get_object_or_404(CoachingSession, id=id)
    if request.method == "GET":
        booked_session.delete()
        return HttpResponseRedirect("/booking?offset=" + str(offset_param))
    return render(request, "booking/booking.html", context)

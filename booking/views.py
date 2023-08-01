from django.shortcuts import render
from datetime import datetime, timezone
# Create your views here.


def booking(request):

    local = datetime.now()
    time_utc = datetime.utcnow()


    local_conv = local.strftime("%m/%d/%Y, %H:%M:%S")
    time_utc_conv = time_utc.strftime("%m/%d/%Y, %H:%M:%S")
    dt_now_conv = time_utc.strftime("%m/%d/%Y, %H:%M:%S")

    today_to_utc_conv = local.utcnow().strftime("%m/%d/%Y, %H:%M:%S")

    date = 1
    return render(request, 'booking.html', {'date': date})
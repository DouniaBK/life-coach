
from django.contrib import admin
from .models import CoachingSession
from .forms import CoachingSessionInputForm


# Appointment model is in the booking app


@admin.register(CoachingSession)
class CoachingSessionAdmin(admin.ModelAdmin):
    model = CoachingSession
    list_display = ("user", "service", "time", "duration")
    list_filter = ("user", "service", "time", "duration")
    search_fields = ("user", "service", "time", "duration")
    ordering = ('time',)

    form = CoachingSessionInputForm

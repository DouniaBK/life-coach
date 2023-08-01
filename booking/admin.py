from django.contrib import admin
from .models import Appointment


# Appointment model is in the booking app


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = ("user", "service", "time")
    list_filter = ("user", "service", "time")
    search_fields = ("user", "service", "time")
    ordering = ("time",)
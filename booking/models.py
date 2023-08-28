from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils import timezone
from coachapp.models import CustomUser
from datetime import timedelta, date, time


# Create your models here.

COACHING_SERVICES_CHOICES = (
    ("Freedom and Thrive", "Freedom and Thrive"),
    ("Ignite Your Potential", "Ignite Your Potential"),
    ("Unleash Your Extraordinary Life", "Unleash Your Extraordinary Life"),
    ("Breakthrough to Freedom", "Breakthrough to Freedom"),
    )


class CoachingSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)   # noqa
    service = models.CharField(max_length=200, choices=COACHING_SERVICES_CHOICES, default="")   # noqa
    time = models.DateTimeField(default=datetime.now, blank=True)
    duration = models.DurationField(default=timedelta(minutes=60))

    def __str__(self):
        return f'{self.user} | service: {self.service}'

# Generated by Django 3.2.20 on 2023-08-03 18:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_coachingsession'),
    ]

    operations = [
        migrations.AddField(
            model_name='coachingsession',
            name='duration',
            field=models.DurationField(default=datetime.timedelta(seconds=3600)),
        ),
        migrations.AddField(
            model_name='coachingsession',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
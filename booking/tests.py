from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import CoachingSession, COACHING_SERVICES_CHOICES
from datetime import datetime, timedelta, date, time
from .views import getDaysOfWeekForDay, sortSessionsByDay
import pytz

# Create your tests here.

class BookingTests(TestCase):

    # Test the creation of a session
    def test_create_session(self):

        # Create a user for the session
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.de", password="dodo")
        self.assertTrue(True)
        t = datetime.now()
        session = CoachingSession.objects.create(user=user, service='Freedom and Thrive', time=t, duration=timedelta(minutes=60))
        session.save()
        
        all_user_sessions = CoachingSession.objects.filter(user=user)
        print('all_user_sessions')
        print(all_user_sessions)

        self.assertEqual(len(all_user_sessions), 1)
        for s in all_user_sessions:
            print(s)
            self.assertEqual(s.user, user)
            self.assertEqual(s.service, "Freedom and Thrive")
            self.assertEqual(s.time, t)
            self.assertEqual(s.duration, timedelta(minutes=60))
        


    def test_subfunctions(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.de", password="dodo")
        self.assertTrue(True)
        t = datetime(2023,8,15,8,0,0)
        session1 = CoachingSession.objects.create(user=user, service='Freedom and Thrive', time=t, duration=timedelta(minutes=60))
        session1.save()
        session2 = CoachingSession.objects.create(user=user, service='Freedom and Thrive', time=t+timedelta(hours=1), duration=timedelta(minutes=60))
        session2.save()
        session3 = CoachingSession.objects.create(user=user, service='Freedom and Thrive', time=t+timedelta(hours=2), duration=timedelta(minutes=60))
        session3.save()
        session4 = CoachingSession.objects.create(user=user, service='Freedom and Thrive', time=t+timedelta(hours=3), duration=timedelta(minutes=60))
        session4.save()

        days_of_the_week, weekday = getDaysOfWeekForDay(t)
        self.assertEqual(weekday, 1)
        self.assertEqual(days_of_the_week[0], '08/14/2023') # Monday
        self.assertEqual(days_of_the_week[6], '08/20/2023') # Sunday

        # Check in database for existing sessions during that week
        start_dt = t.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=(0-weekday))
        end_dt = start_dt + timedelta(days=7)
        all_sessions = CoachingSession.objects.filter(time__gte=start_dt, time__lt=end_dt)

        sessions_of_the_week = sortSessionsByDay(all_sessions, days_of_the_week, user)

        for d in days_of_the_week:
            if d == weekday: 
                self.assertEqual(len(sessions_of_the_week[d]), 4)
            else:
                self.assertEqual(len(sessions_of_the_week[d]), 0)

from django.contrib.auth import get_user_model
from django.test import TestCase
from .models import Testimonial


class UsersManagersTests(TestCase):
    # Created following Michael Herman guide to testing mentioned on the Readme
    def test_create_user(self):
        print("Test normal user")
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.de", password="dodo")   # noqa
        self.assertEqual(user.email, "normal@user.de")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    # Created following Michael Herman guide to testing mentioned on the Readme
    def test_create_superuser(self):
        print("Test super user")
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.de", password="dodo")   # noqa
        self.assertEqual(admin_user.email, "super@user.de")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_create_testimonial(self):
        testimonial = Testimonial.objects.create(name='TestImonial', body='The testimonial is a test', status=0)   # noqa
        testimonial.save()

        self.assertEqual(testimonial.name, 'TestImonial')
        self.assertEqual(testimonial.body, 'The testimonial is a test')
        self.assertEqual(testimonial.status, 0)

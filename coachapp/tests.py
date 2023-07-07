from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.


class UsersManagersTests(TestCase):

    def text_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(emai="normal@user.de", password="dodo")
        self.assertEqual(user.email, "normal@user.de")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(TypeError):
            User.objects.create_user(email="", password="dodo")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.de", password="dodo")  # noqa
        self.assertEqual(admin_user.email, "super@user.de")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

        with self.assertRaises(TypeError):
            User.objects.create_superuser(email="super@user.de", password="dodo", is_superuser=False)  # noqa

from django.contrib.auth import get_user_model
from django.test import TestCase

class UsersManagersTests(TestCase):

    def test_create_user(self):
        print("Test normal user")
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.de", password="dodo")
        self.assertEqual(user.email, "normal@user.de")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        print("Test super user")
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.de", password="dodo")
        print(admin_user) # noqa
        self.assertEqual(admin_user.email, "super@user.de")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        
        #with self.assertRaises(ValueError):
        #    User.objects.create_superuser(email="superduper@user.de", password="dodo", is_superuser=True)  # noqa


from django.contrib.auth.base_user import BaseUserManager


class CustomUserManager(BaseUserManager):
    """ An email is needed for authentification """
    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("A valid Email address must be entered"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """ Create and save a Superuser with the given email and password """
        print("create_superuser")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff set to True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser set to True."))
        return self.create_user(email, password, **extra_fields)
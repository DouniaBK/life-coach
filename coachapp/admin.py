from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Testimonial


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("email", 'first_name', 'last_name', "is_staff", "is_active")
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {"fields": ("email", "password", 'first_name', 'last_name', 'address')}),
        ("Permissions", {"fields": ("is_staff", "is_active", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email",'first_name', 'last_name', 'address', "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}),
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


@admin.register(Testimonial)
class TestimonyAdmin(admin.ModelAdmin):

    list_display = ('name', 'status')
    list_filter = ('status', 'name')
    search_fields = ('name', 'status')


admin.site.register(CustomUser, CustomUserAdmin)

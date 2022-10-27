from django.contrib import admin
from . models import CustomUser
from django.contrib.auth.admin import UserAdmin

from . forms import CustomeUserCreationForm,    CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomeUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'name', 'is_staff']


admin.site.register(CustomUser, CustomUserAdmin)
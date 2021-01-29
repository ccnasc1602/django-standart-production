# -*- encoding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth import admin as auth_admin

from .forms import UserCreationForm
from .models import User


class UserAdmin(auth_admin.UserAdmin):
    add_form = UserCreationForm
    model = User
    list_display = ['username', 'mobile_number', 'birth_date']
    fieldsets = auth_admin.UserAdmin.fieldsets + (
        (None, {'fields': ('mobile_number', 'birth_date')}),
    )

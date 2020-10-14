from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

from .models import Team, CustomUser


@admin.register(CustomUser)
class UserAdmin(DefaultUserAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    fields = (
        'name', 'position', 'biography', 'linkedin', 'twitter', 'created_date', 'updated_date',
    )
    list_display = (
        'name', 'position', 'biography', 'linkedin', 'twitter', 'created_date', 'updated_date',
    )
    readonly_fields = (
        'created_date', 'updated_date',
    )

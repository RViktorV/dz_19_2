from django.contrib import admin

from users.models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "email")
    search_fields = ("email",)
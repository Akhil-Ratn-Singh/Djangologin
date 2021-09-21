from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
fields = list(UserAdmin.fieldsets)
fields[0] = (None, {'fields': ('username', 'password', 'address')})
UserAdmin.fieldsets = tuple(fields)

admin.site.register(User, UserAdmin)
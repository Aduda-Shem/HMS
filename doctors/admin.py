from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Doctor, Nurse

class DoctorInline(admin.StackedInline):
    model = Doctor
    can_delete = False

class NurseInline(admin.StackedInline):
    model = Nurse
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (DoctorInline, NurseInline)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

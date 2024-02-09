from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, HealthcareProfessional, Patient

class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ( 'email', 'image')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'first_name', 'last_name', 'email', 'phone_number'),
        }),
    )

    def register_user(self, request, queryset):
        for user in queryset:
            user.is_active = True  
            user.save()

        self.message_user(request, 'Selected users have been registered successfully.')

    register_user.short_description = 'Register selected users'

admin.site.register(User, CustomUserAdmin)

@admin.register(HealthcareProfessional)
class HealthcareProfessionalAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'specialization', 'license_number', 'date_of_birth')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('role',)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_of_birth', 'gender')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    list_filter = ('gender',)


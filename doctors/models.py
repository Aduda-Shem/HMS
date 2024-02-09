from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
    username = models.CharField(_('Username'), max_length=150, unique=True, blank=True, null=True)
    email = models.EmailField(_('Email Address'), unique=True, null=False, db_index=True)
    image = models.ImageField(upload_to='media/profile_pics/', blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return str(self.email)


class HealthcareProfessional(models.Model):
    ROLE_CHOICES = [
        ('doctor', 'Doctor'),
        ('nurse', 'Nurse'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='healthcare_professional')
    email = models.EmailField(_('Email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    role = models.CharField(_('Role'), max_length=10, choices=ROLE_CHOICES)
    specialization = models.CharField(_('Specialization'), max_length=100, blank=True, null=True)
    license_number = models.CharField(_('License number'), max_length=50)
    date_of_birth = models.DateField(_('Date of birth'))
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = _('Healthcare Professional')
        verbose_name_plural = _('Healthcare Professionals')

    def __str__(self):
        return self.email


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient')
    email = models.EmailField(_('Email address'), unique=True)
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    date_of_birth = models.DateField(_('Date of birth'))
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(_('Gender'), max_length=1, choices=GENDER_CHOICES)

    class Meta:
        verbose_name = _('Patient')
        verbose_name_plural = _('Patients')

    def __str__(self):
        return self.email

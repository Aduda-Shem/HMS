from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from doctors.managers import UserManager

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    specialization = models.CharField(_('specialization'), max_length=100)
    license_number = models.CharField(_('license number'), max_length=50)
    date_of_birth = models.DateField(_('date of birth'))
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(_('gender'), max_length=1, choices=GENDER_CHOICES)
    is_doctor = models.BooleanField(_('is doctor'), default=True)

    class Meta:
        verbose_name = _('doctor')
        verbose_name_plural = _('doctors')

    def __str__(self):
        return self.email

class Nurse(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=50)
    last_name = models.CharField(_('last name'), max_length=50)
    phone = models.CharField(_('phone number'), max_length=15, unique=True)
    assigned_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='nurses', null=True, blank=True)
    is_nurse = models.BooleanField(_('is nurse'), default=True)
    license_number = models.CharField(_('license number'), max_length=50)

    class Meta:
        verbose_name = _('nurse')
        verbose_name_plural = _('nurses')

    def __str__(self):
        return self.email

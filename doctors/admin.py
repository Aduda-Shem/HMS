from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _
from doctors.managers import UserManager

class User(AbstractUser):
    username = models.CharField(_('Username'), max_length=150, unique=True, blank=True, null=True)
    first_name = models.CharField(_('First Name'), max_length=100, blank=True, null=True)
    last_name = models.CharField(_('Last Name'), max_length=100, blank=True, null=True)
    email = models.EmailField(_('Email Address'), unique=True, null=False, db_index=True)
    phone_number = models.CharField(_('Phone Number'), max_length=100, blank=False, null=False)
    national_id = models.IntegerField(_('National Identification Number'), blank=True, null=True)
    image = models.ImageField(upload_to='media/profile_pics/', blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    groups = models.ManyToManyField(Group, verbose_name=_('groups'), blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='custom_user_set',
    )

    def __str__(self):
        return str(self.email)

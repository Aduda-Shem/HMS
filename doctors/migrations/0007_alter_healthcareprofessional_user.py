# Generated by Django 4.2.7 on 2024-02-11 14:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_alter_healthcareprofessional_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='healthcareprofessional',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
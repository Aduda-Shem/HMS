# Generated by Django 4.2.7 on 2024-04-02 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_remove_medicalrecord_admission_charges_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalrecord',
            name='price',
        ),
    ]

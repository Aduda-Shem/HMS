# Generated by Django 4.2.7 on 2024-04-02 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_remove_schedule_doctor_schedule_data_schedule_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedule',
            name='title',
            field=models.CharField(default=1, max_length=50, verbose_name='Title'),
            preserve_default=False,
        ),
    ]

# Generated by Django 4.2.7 on 2024-04-04 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_alter_invoice_options_remove_invoice_reference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]

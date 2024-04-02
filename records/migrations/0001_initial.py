# Generated by Django 4.2.7 on 2024-04-02 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FileNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20, unique=True)),
                ('patient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='file_number', to='doctors.patient')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prescription', models.TextField(blank=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('blood_pressure', models.CharField(blank=True, max_length=20, null=True)),
                ('heart_rate', models.CharField(blank=True, max_length=20, null=True)),
                ('temperature', models.CharField(blank=True, max_length=20, null=True)),
                ('weight', models.CharField(blank=True, max_length=20, null=True)),
                ('height', models.CharField(blank=True, max_length=20, null=True)),
                ('lab_results', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('total_charges', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('allergies', models.TextField(blank=True)),
                ('medications', models.TextField(blank=True)),
                ('admission_charges', models.TextField(blank=True)),
                ('treatment_charges', models.TextField(blank=True)),
                ('medication_charges', models.TextField(blank=True)),
                ('diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='records.diagnosis')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.healthcareprofessional')),
                ('file_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_records', to='records.filenumber')),
            ],
        ),
        migrations.CreateModel(
            name='Medication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medications_records', to='records.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='TreatmentCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='treatment_charges_records', to='records.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='symptoms', to='records.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='MedicationCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_charges_records', to='records.medicalrecord')),
                ('medication', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medication_charges', to='records.medication')),
            ],
        ),
        migrations.CreateModel(
            name='Allergy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='allergies_records', to='records.medicalrecord')),
            ],
        ),
        migrations.CreateModel(
            name='AdmissionCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('medical_record', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='admission_charges_records', to='records.medicalrecord')),
            ],
        ),
    ]

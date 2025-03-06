# Generated by Django 5.1.6 on 2025-03-05 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
        ('App2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patients',
            name='doctor',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='patients',
            name='updated_by',
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Gender', models.CharField(default='', max_length=10)),
                ('Specialist', models.CharField(default='', max_length=40)),
                ('isActive', models.BooleanField(default=False, help_text='0-Inactive,1-active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Doctors_created', to='App2.receptionist')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Doctors_updated', to='App2.receptionist')),
            ],
        ),
        migrations.CreateModel(
            name='patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=20)),
                ('Age', models.CharField(default='', max_length=20)),
                ('Initial_Disease', models.CharField(default='', max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Patients_created', to='App2.receptionist')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App1.doctor')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patients_updated', to='App2.receptionist')),
            ],
        ),
        migrations.DeleteModel(
            name='Doctors',
        ),
        migrations.DeleteModel(
            name='Patients',
        ),
    ]

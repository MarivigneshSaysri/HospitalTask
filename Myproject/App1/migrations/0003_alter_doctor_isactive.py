# Generated by Django 5.1.6 on 2025-03-05 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0002_remove_patients_doctor_remove_patients_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='isActive',
            field=models.BooleanField(default=True, help_text='0-Inactive,1-active'),
        ),
    ]

# Generated by Django 4.0.10 on 2024-06-22 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0012_rename_previnfection_hbv_patient_previnfection_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='emailaddress',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
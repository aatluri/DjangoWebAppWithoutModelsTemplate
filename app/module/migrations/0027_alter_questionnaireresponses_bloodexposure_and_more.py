# Generated by Django 4.0.10 on 2024-07-05 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0026_questionnaireresponses_remove_patient_bloodexposure_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaireresponses',
            name='bloodexposure',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponses',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponses',
            name='drinkingstatus',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponses',
            name='previnfection',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='questionnaireresponses',
            name='smokingstatus',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]

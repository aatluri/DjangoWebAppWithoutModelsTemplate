# Generated by Django 4.0.10 on 2024-06-22 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_rename_caption_tag_tagname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diagnostictest',
            name='tags',
            field=models.ManyToManyField(blank=True, to='module.tag'),
        ),
    ]

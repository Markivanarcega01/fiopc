# Generated by Django 5.2 on 2025-05-05 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0005_alter_application_cv'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobopportunity',
            name='qualifications',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='jobopportunity',
            name='requirements',
            field=models.TextField(blank=True),
        ),
    ]

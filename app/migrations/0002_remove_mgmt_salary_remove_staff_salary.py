# Generated by Django 5.1.3 on 2024-11-29 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mgmt',
            name='salary',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='salary',
        ),
    ]

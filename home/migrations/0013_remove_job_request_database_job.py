# Generated by Django 3.1.2 on 2022-09-04 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_job_request_database_job'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_request_database',
            name='job',
        ),
    ]

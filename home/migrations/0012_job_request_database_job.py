# Generated by Django 3.1.2 on 2022-09-04 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20220904_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_request_database',
            name='job',
            field=models.ManyToManyField(related_name='job_request_databases', to='home.job_database'),
        ),
    ]

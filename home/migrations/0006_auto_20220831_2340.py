# Generated by Django 3.1.2 on 2022-08-31 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_job_database'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_database',
            name='job_amount',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]

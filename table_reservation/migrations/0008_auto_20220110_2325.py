# Generated by Django 3.2 on 2022-01-10 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_reservation', '0007_auto_20220106_2343'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='time_and_date',
        ),
        migrations.AddField(
            model_name='reservation',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='time',
            field=models.TimeField(blank=True, default=None, null=True),
        ),
    ]

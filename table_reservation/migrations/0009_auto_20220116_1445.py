# Generated by Django 3.2 on 2022-01-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_reservation', '0008_auto_20220110_2325'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(blank=True, default=None, max_length=50, null=True),
        ),
    ]

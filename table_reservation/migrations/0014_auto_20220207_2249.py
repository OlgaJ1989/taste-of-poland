# Generated by Django 3.2 on 2022-02-07 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table_reservation', '0013_alter_reservation_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='first_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='last_name',
            field=models.CharField(default=None, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='party_size',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='time',
            field=models.TimeField(default=None, null=True),
        ),
    ]

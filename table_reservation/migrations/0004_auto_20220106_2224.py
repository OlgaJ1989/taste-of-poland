# Generated by Django 3.2 on 2022-01-06 22:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('table_reservation', '0003_remove_reservation_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.IntegerField()),
                ('min_people', models.IntegerField()),
                ('max_people', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='additional_info',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='created_on',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='email',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='party_size',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='time_and_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='updated_on',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='user',
        ),
        migrations.AddField(
            model_name='reservation',
            name='spot',
            field=models.DateField(default=None),
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='booking_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='reservation',
            name='party',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='table_reservation.customer'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='table',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='table_reservation.table'),
        ),
    ]

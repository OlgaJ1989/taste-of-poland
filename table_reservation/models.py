import datetime
from django.db import models
from django.contrib.auth.models import User


TIME_CHOICES = (
    ("12:00", "12:00"),
    ("13:00", "13:00"),
    ("14:00", "14:00"),
    ("15:00", "15:00"),
    ("16:00", "16:00"),
    ("17:00", "17:00"),
    ("18:00", "18:00"),
    ("19:00", "19:00"),
    ("20:00", "20:00"),
    ("21:00", "21:00"),
    ("22:00", "22:00"),
)

PEOPLE_CHOICES = (
    (1, "1 person"),
    (2, "2 people"),
    (3, "3 people"),
    (4, "4 people"),
    (5, "5 people"),
    (6, "6 people"),
)


# class Customer(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="booking_user",
#         default=None)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()


class Table(models.Model):
    table_name = models.CharField(default=None, max_length=20, unique=True)
    max_people = models.IntegerField()

    def __str__(self):
        return self.table_name


class Reservation(models.Model):
    table = models.ForeignKey(
        'Table', on_delete=models.CASCADE, default=None, null=True)
    booker = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True)
    first_name = models.CharField(
        max_length=50, default=None, blank=False, null=True,)
    last_name = models.CharField(
        max_length=50, default=None, blank=False, null=True)
    party_size = models.IntegerField(
        default=1, blank=False, choices=PEOPLE_CHOICES)
    date = models.DateField(
        blank=False, null=True, default=datetime.date.today)
    time = models.CharField(
        max_length=10, default="12:00", choices=TIME_CHOICES, blank=False,
        null=True)
    additional_info = models.TextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_on', '-created_on']

    def __str__(self):
        return '%s %s %s %s' % (
            self.first_name, self.last_name, self.date, self.time)


# class Reservation(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="booking_user",
#         default=None)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()
#     # status
#     time_and_date = models.DateTimeField()
#     created_on = models.DateTimeField(auto_now_add=True)
#     updated_on = models.DateTimeField(auto_now=True)
#     party_size = models.IntegerField(default=1)
#     additional_info = models.TextField(blank=True, null=True)
#     approved = models.BooleanField(default=False)

#     def __str__(self):
#         return self.title

#     def __str__(self):
#         return '%s %s' % (self.first_name, self.last_name)

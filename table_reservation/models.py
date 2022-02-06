from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# class Customer(models.Model):
#     user = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name="booking_user",
#         default=None)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField()


class Table(models.Model):
    # seats = models.IntegerField()
    min_people = models.IntegerField()
    max_people = models.IntegerField()


class Reservation(models.Model):
    table = models.ForeignKey(
        'Table', on_delete=models.CASCADE, default=None, null=True)
    booker = models.ForeignKey(
        User, on_delete=models.CASCADE, default=None, null=True)
    first_name = models.CharField(
        max_length=50, default=None, blank=True, null=True)
    last_name = models.CharField(
        max_length=50, default=None, blank=True, null=True)
    party_size = models.IntegerField(default=1)
    date = models.DateField(blank=True, null=True)
    time = models.TimeField(default=None, blank=True, null=True)
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

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_user")
    first_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_fname")
    last_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_lname")
    email = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_email")
    # status 
    time_and_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    party_size = models.IntegerField(default=1)
    additional_info = models.TextField(blank=True, null=True)
    name = models.TextField()

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

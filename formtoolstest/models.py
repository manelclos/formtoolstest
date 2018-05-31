from django.db import models
from django.contrib.auth.models import User


class Booking(models.Model):
    name = models.CharField(max_length=30)
    primary_user = models.ForeignKey(User, on_delete=models.CASCADE)


class TicketPerson(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    email = models.CharField(max_length=50)

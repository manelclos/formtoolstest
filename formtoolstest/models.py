from django.db import models


class Booking(models.Model):
    name = models.CharField(max_length=30)


class BookingPerson(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

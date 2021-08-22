from django.db import models


class Vehicle(models.Model):

    license_plate = models.CharField(max_length=6, unique=True)
    model = models.IntegerField()
    brand = models.CharField(max_length=200)
    type_vehicle = models.CharField(max_length=110)



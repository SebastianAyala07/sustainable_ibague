from django.db import models
from persons.models import Driver, Student


class Vehicle(models.Model):

    license_plate = models.CharField(max_length=6, unique=True)
    model = models.IntegerField()
    brand = models.CharField(max_length=200)
    type_vehicle = models.CharField(max_length=110)
    photo = models.ImageField(upload_to='vehicles/')
    maximum_passengers = models.IntegerField()
    fuel_type = models.CharField(max_length=255)
    driver = models.ForeignKey(Driver, on_delete=models.PROTECT)
    available = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"{self.license_plate} - {self.brand} {self.model}"


class Service(models.Model):

    vehicle_id = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    students_id = models.ManyToManyField(Student, blank=True)
    date = models.DateField()
    time = models.TimeField()
    address = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.vehicle_id} - {self.date}"

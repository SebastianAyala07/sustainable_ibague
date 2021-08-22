from django.db import models


class Person(models.Model):

    identification_card = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    surnames = models.CharField(max_length=150)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        abstract = True


class Student(Person):

    institution = models.CharField(max_length=255)
    accumulated_miles = models.IntegerField()


class Driver(Person):

    type_of_license = models.CharField(max_length=255)
    license_issue_date = models.DateField()

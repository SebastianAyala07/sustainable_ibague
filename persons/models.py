from django.db import models


class Person(models.Model):

    identification_card = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=150)
    surnames = models.CharField(max_length=150)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='persons/')
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.name} {self.surnames}"


class Student(Person):

    institution = models.CharField(max_length=255)
    accumulated_miles = models.IntegerField(default=0)


class Driver(Person):

    type_of_license = models.CharField(max_length=255)
    license_issue_date = models.DateField()

from django.db import models

class Employee(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    age = models.SmallIntegerField()
    phoneNumber = models.CharField(max_length=12)
    email = models.CharField(max_length=40)

    def __repr__(self):
        return f"{self.firstName} {self.lastName}"

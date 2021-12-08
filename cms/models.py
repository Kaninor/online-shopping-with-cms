from django.db import models

class CMSUser(models.Model):
    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    age = models.SmallIntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=50)
    role = models.CharField(max_length=15)
    id_card = models.CharField(max_length=10)

    def __repr__(self):
        return f"{self.firstName} {self.lastName}"

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

class Product(models.Model):
    name = models.CharField(max_length=30, unique=True)
    number = models.BigIntegerField()
    off = models.FloatField()
    added_in = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

class PubFile(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=15)
    file = models.FileField(upload_to="pub files")
    added_in = models.DateTimeField(auto_now_add=True)

    def delete(self, using=None, keep_parents=False):
        self.file.storage.delete(self.file.name)
        super().delete()

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name
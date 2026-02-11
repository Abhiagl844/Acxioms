from django.db import models


class Vendors(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    vendor_email = models.EmailField()
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='products/',null=True,blank=True)
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.name

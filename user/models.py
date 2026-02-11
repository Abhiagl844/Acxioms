from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Cart(models.Model):
    user_email = models.EmailField()
    product = models.ForeignKey('vendor.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()

class requestItem(models.Model):
    name = models.CharField(max_length=200)

class UserRequest(models.Model):
    user_email = models.EmailField()
    item_name = models.CharField(max_length=200)
    status = models.CharField(max_length=50, default="Pending")



class Order(models.Model):

    STATUS_CHOICES = [
        ('Received', 'Received'),
        ('Ready for Shipping', 'Ready for Shipping'),
        ('Out For Delivery', 'Out For Delivery'),
    ]

    user_email = models.EmailField()
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    total_price = models.IntegerField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Received')

    def __str__(self):
        return self.product_name

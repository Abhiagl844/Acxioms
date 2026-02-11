from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Membership(models.Model):

    DURATION_CHOICES = [
        ('6', '6 Months'),
        ('12', '1 Year'),
        ('24', '2 Years'),
    ]

    membership_number = models.CharField(max_length=20, unique=True)
    user_email = models.EmailField()
    duration = models.CharField(max_length=2, choices=DURATION_CHOICES, default='6')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.membership_number

from django.db import models
from django.contrib.auth.models import User


class Account(User):
    address = models.CharField(max_length=34, blank=False, null=False)


class Product(models.Model):
    account = models.ForeignKey(Account, blank=False, null=False)


class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('CR', 'Created'),
        ('CH', 'Checked')
    )
    
    
    state = models.CharField(max_length=2, choices=PAYMENT_CHOICES, default="CR")
    input_address = models.CharField(max_length=34)
    product = models.ForeignKey(Product, blank=False, null=False)
    

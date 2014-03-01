from django.db import models
from django.contrib.auth.models import User


class Account(User):
    address = models.CharField(max_length=34, blank=False, null=False)


class Product(models.Model):
    account = models.ForeignKey(Account, blank=False, null=False)
    price = models.DecimalField(max_digits=6, decimal_places=4, blank=False, null=False)
    description = models.CharField(max_length=250)
    name = models.CharField(max_length=40)
    image_1 = models.ImageField(upload_to="/media", blank=False, null=False)
    image_2 = models.ImageField(upload_to="/media")
    app = models.FileField(upload_to="/media", blank=False, null=False)
    
    def __unicode__(self):
        return "Product #" + str(self.id)

class Payment(models.Model):
    PAYMENT_CHOICES = (
        ('CR', 'Created'),
        ('CH', 'Checked')
    )
    
    
    state = models.CharField(max_length=2, choices=PAYMENT_CHOICES, default="CR")
    input_address = models.CharField(max_length=34)
    product = models.ForeignKey(Product, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)

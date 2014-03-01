from django.db import models
from django.contrib.auth.models import User


class Account(User):
    address = models.CharField(max_length=34, blank=False, null=False)


class Product(models.Model):
    models.ForeignKey(Account, blank=False, null=False)

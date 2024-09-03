from django.db import models

# Create your models here.

class ProductTable(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    category = models.CharField(max_length=20)
    availability = models.CharField(max_length=20)

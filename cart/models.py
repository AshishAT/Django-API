from django.db import models

# Create your models here.

class Cart(models.Model):
    username = models.CharField(max_length=100)
    product_id = models.CharField(max_length=100)
    quntity = models.IntegerField()

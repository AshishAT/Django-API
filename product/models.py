from django.db import models

# Create your models here.

class Brand(models.Model):
    company_name = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=100)

class Product_Category(models.Model):
    category_name = models.CharField(max_length=100)

class Products(models.Model):
    product_id = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    category_name = models.ForeignKey(Product_Category,on_delete=models.CASCADE)

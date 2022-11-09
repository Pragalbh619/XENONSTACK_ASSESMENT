from django.db import models

# Create your models here.
class category(models.Model):
    category=models.CharField(max_length=50)
    
class product(models.Model):
    category_name=models.CharField(max_length=50)
    product_name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.CharField(max_length=50)
    details=models.CharField(max_length=50) 
    
class product2(models.Model):
    category_name=models.CharField(max_length=50)
    product_name=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    image=models.CharField(max_length=50)
    details=models.CharField(max_length=50) 
    
class purchase(models.Model):
    category=models.CharField(max_length=50)
    product=models.CharField(max_length=50)
    price=models.CharField(max_length=50)
    emails=models.CharField(max_length=50)
    address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
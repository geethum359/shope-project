from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Products(models.Model):
    pro_name= models.CharField(max_length=255)
    pro_price= models.IntegerField()
    pro_image = models.ImageField(upload_to='proimages' ,null=True, blank=True)
    description=models.CharField(max_length=225)
    category=models.ForeignKey(category,on_delete=models.CASCADE)
    def __str__(self):
        return self.pro_name


class CustomUser(AbstractUser):
    email=models.EmailField()
    phone=models.CharField(max_length=10,null=True, blank=True)


class Cart(models.Model):
    items = models.ManyToManyField(Products, through='CartItem')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    stock = models.IntegerField(default=0)
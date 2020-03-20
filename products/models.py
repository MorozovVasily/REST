from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.IntegerField()
    owner = models.ForeignKey('auth.User', related_name='products', on_delete=models.CASCADE)

from django.db import models


class Chip(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    company = models.CharField(max_length=100)

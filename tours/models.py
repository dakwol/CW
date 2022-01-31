from django.db import models


# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)


class Town(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)


class Hotel(models.Model):
    name = models.CharField(max_length=100)
    town = models.ForeignKey(Town, on_delete=models.CASCADE, default=None)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)


class Tour(models.Model):
    name = models.CharField(max_length=100)
    date_start = models.DateField()
    date_end = models.DateField()
    price = models.IntegerField()
    tickets_max = models.IntegerField()
    tickets_now = models.IntegerField()
    description = models.TextField()
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)
    towns = models.ManyToManyField(Town)
    hotels = models.ManyToManyField(Hotel)

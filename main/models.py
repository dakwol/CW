from django.db import models
from django.contrib.auth.models import *


# Create your models here
class Card(models.Model):
    Name = models.TextField()
    Date = models.TextField()
    CVV = models.TextField()
    Balance = models.IntegerField(default=0)


class Country(models.Model):
    name = models.CharField(max_length=100)


class Town(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)


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
    pic = models.TextField(default="/static/images/Exotic-tropical-beach-sunse.jpg")


class Ticket(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, default=None)
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

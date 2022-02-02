from django.db import models


# Create your models here
class Card(models.Model):
    Number = models.TextField()
    Date = models.TextField()
    CVV = models.TextField()

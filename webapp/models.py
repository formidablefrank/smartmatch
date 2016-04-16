from django.db import models

# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length = 50)
    hla = models.CharField(max_length = 20)
    age = models.IntegerField(default = 0)
    weight = models.DecimalField(decimal_places = 2, max_digits = 5)

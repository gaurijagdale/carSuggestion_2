from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    # logo_url = models.URLField()

    def __str__(self):
        return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='car_images/')  # Use ImageField for storing images
    price = models.FloatField()
    fin_price=models.FloatField(null=True)
    fuel_type = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name
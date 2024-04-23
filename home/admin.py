from django.contrib import admin
from .models import (
    Brand,
    CarModel
)

@admin.register(CarModel)
class CarModelModelAdmin(admin.ModelAdmin):
    list_display=['id','brand','name','image','price','fin_price','fuel_type','transmission','mileage']

@admin.register(Brand)
class BrandModelAdmin(admin.ModelAdmin):
    list_display=['name']
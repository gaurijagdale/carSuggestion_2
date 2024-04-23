from django.shortcuts import render, get_object_or_404
from .models import Brand, CarModel

# Create your views here.
def index(request):
    return render(request, "home.html")

def home(request):
    return render(request, "home.html")

def findCars(request):
    return render(request, "findCars.html")

def brands(request):
    return render(request, "brands.html")

def autoguide(request):
    return render(request, "autoguide.html")

def brand_detail(request, brand_name):
    brand = get_object_or_404(Brand, name=brand_name)
    models = brand.carmodel_set.all()  # Retrieve all car models for this brand
    return render(request, 'kia.html', {'brand': brand, 'models': models})


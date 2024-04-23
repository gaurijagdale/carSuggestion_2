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


def kia(request):
    # Fetch brand and models data for Kia
    brand = Brand.objects.get(name='Kia')
    models = CarModel.objects.filter(brand=brand)
    return render(request, 'kia.html', {'brand': brand, 'models': models})

def renault(request):
    brand = Brand.objects.get(name='Renault')
    models = CarModel.objects.filter(brand=brand)
    return render(request, 'kia.html', {'brand': brand, 'models': models})

def toyota(request):
    brand = Brand.objects.get(name='Toyota')
    models = CarModel.objects.filter(brand=brand)
    return render(request, 'kia.html', {'brand': brand, 'models': models})


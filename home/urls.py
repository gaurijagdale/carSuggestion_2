from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name="home"),
    # path("home/", views.index, name="home"),
    path("findCars", views.findCars, name="findCars"),
    path("brands", views.brands, name="brands"),
    path("autoguide", views.autoguide, name="autoguide"),

    path('brands/<str:brand_name>/', views.brand_detail, name='brand_detail'),
    


]

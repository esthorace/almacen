from django.urls import path
from almacen import views

ulrpatterns = [
    path('', views.index, name="index"),
]
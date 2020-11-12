from django.contrib import admin
from django.urls import path
from .views import CategoriaShowView

app_name = 'prueba'

urlpatterns = [
   path('categoria/<int:pk>/', CategoriaShowView.as_view(), name='categoria_show')
]

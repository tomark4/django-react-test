from django.contrib import admin
from django.urls import path
from .views import IndexView, PruebaView

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('prueba/',PruebaView.as_view(), name='prueba')
]

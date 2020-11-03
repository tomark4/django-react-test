from django.contrib import admin
from django.urls import path
from .views import ListView, DetailView
app_name = 'api'

urlpatterns = [
    path('detail/', DetailView.as_view(), name='detail'),
    path('list/', ListView.as_view(), name='list'),
]

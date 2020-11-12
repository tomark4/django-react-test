from rest_framework import serializers
from .models import Categoria, Entrada

""" add comment in serializer"""
class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        depth = 1

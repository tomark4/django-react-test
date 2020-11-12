from rest_framework import serializers
from .models import Categoria, Entrada

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        depth = 1

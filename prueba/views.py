from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import CategoriaSerializer
from .models import Categoria
from django.http import Http404
from rest_framework.response import Response
# Create your views here.

class CategoriaShowView(APIView):

    def get_object(self, pk):
        try:
            return Categoria.objects.get(pk=pk)
        except Categoria.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serializer = CategoriaSerializer(snippet)
        return Response(serializer.data)


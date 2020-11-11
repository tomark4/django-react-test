from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import JsonResponse
# Create your views here.

class IndexView(TemplateView):
    template_name = 'blog/index.html'

class PruebaView(TemplateView):
    #template_name = 'blog/index.html'

    def get(self, request, *args, **kwargs):
        data = [
            {'id':'1', 'name':'jose'},
            {'id':'2', 'name':'peter'}
        ]
        return JsonResponse({'usuarios': data})

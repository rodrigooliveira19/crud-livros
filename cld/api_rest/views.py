from django.shortcuts import render

from livros import models
from api_rest import serializers
from rest_framework import generics

# Create your views here.

class LivroListServiceView(generics.ListCreateAPIView):
	queryset = models.Livro.objects.all()
	serializer_class = serializers.LivroSerializer 


from django.shortcuts import render
from django.http import HttpResponse

from . import urls

# Create your views here.

def index(request):
	return HttpResponse("Olá, Mundo. Vocé está na página index de livros")

def livro_list(request):
	return render(request,'livros/livro_list.html',{})


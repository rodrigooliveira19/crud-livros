from django.shortcuts import render
from django.http import HttpResponse
from .models import Livro
from .forms import LivroForm
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect 

from . import urls

# Create your views here.

def index(request):
	return HttpResponse("Olá, Mundo. Vocé está na página index de livros")

def livro_list(request):
	livros = Livro.objects.order_by('titulo')
	return render(request,'livros/livro_list.html',{'livros':livros})

def livro_new(request):
	if request.method =="POST":
		form = LivroForm(request.POST)
		if form.is_valid():
			livro = form.save(commit=False)
			livro.save()
			return redirect('livro_detail',pk=livro.pk)#
	else:
		form = LivroForm()
		return render(request,'livros/livro_edit.html',{'form':form})

def livro_detail(request, pk):
    livro = get_object_or_404(Livro, pk=pk)
    return render(request, 'livros/livro_detail.html', {'livro': livro})


def livro_edit(request,pk):
	livro = get_object_or_404(Livro,pk=pk) #Retorna o objeto Livro a editar.
	if request.method == "POST":
		form = LivroForm(request.POST,instance=livro)
		if form.is_valid():
			livro = form.save(commit=False)
			livro.save()
			return redirect('livro_detail',pk=livro.pk)
	else:
		form = LivroForm(instance=livro)
	return render(request,'livros/livro_edit.html',{'form':form})


def livro_delete(request,pk):
	livro = get_object_or_404(Livro,pk=pk)
	if request.method =="POST":
		livro.delete()
		return redirect('livro_list')
	else:
		form = LivroForm(instance=livro)
	return render(request,'livros/livro_delete.html',{'livro':livro})




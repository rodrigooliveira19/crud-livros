
from django import forms #importa o modulo de formulário do django. 

from .models import Livro

#LivroFoorm é o nome do formulário. 
# forms.ModelForm diz ao Django  que esse é um modelForm
#Meta diz ao Django qual modelo será utilizado para criar o formulário. 
class LivroForm(forms.ModelForm):

	class Meta:
		model = Livro 
		fields = ('codigo','titulo','autor','ISBN','editora','ano',)
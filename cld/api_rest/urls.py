
from api_rest import views 
from django.urls import path

urlpatterns = [
    path('livros/',views.LivroListServiceView.as_view(),name='livros'),
]
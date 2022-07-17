from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:receita_id>', views.receita, name='receita'),
    path('buscar', views.buscar, name='buscar'),
    path('cria_receita', views.cria_receita, name='cria_receita'),
    path('deletar_receita/<int:receita_id>', views.deletar_receita, name='deletar_receita'),
    path('editar_receita/<int:receita_id>', views.editar_receita, name='editar_receita'),
    path('atualizar_receita', views.atualizar_receita, name='atualizar_receita'),
]
from django.contrib import admin
from .models import Receita 

# Register your models here.
class ListandoReceitas(admin.ModelAdmin):
    list_display = ('id', 'nome_receita', 'categoria', 'publicada')
    list_display_links = ('id', 'nome_receita', 'categoria')
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_editable = ('publicada', )
    list_per_page = 10
admin.site.register(Receita, ListandoReceitas)

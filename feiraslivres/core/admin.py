from django.contrib import admin
from feiraslivres.core.models import FeirasLivres


class FeirasLivresModelAdmin(admin.ModelAdmin):

	list_display = ('id', 'long', 'lat', 'setcens', 'areap', 'coddist', 'distrito',
	                'codsubpref', 'subprefe', 'regiao5', 'regiao8', 'nome_feira',
	                'registro', 'logradouro', 'numero', 'bairro', 'referencia')
	search_fields = ('distrito', 'regiao5', 'nome_feira', 'bairro')
	list_filter = ('distrito', 'regiao5', 'nome_feira', 'bairro')


admin.site.register(FeirasLivres, FeirasLivresModelAdmin)

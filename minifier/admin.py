from django.contrib import admin
from minifier.models import Url

class UrlAdmin(admin.ModelAdmin):

    # Configuration de la liste d'articles
    list_display = ('url', 'code', 'date', 'pseudo', 'access')
    list_filter = ('pseudo', )
    date_hierarchy = 'date'
    ordering = ('date', )
    search_fields = ('url', )

    # Configuration du formulaire d'édition
    

    # prepopulated_fields = {'slug': ('titre', ), }




admin.site.register(Url, UrlAdmin)

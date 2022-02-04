from django.contrib import admin
from .models import *

# Register your models here.
class PlantAdmin(admin.ModelAdmin):
    list_display = ('id', 'scientificName', 'family', 'is_published', 'primaryCommonName')
    list_display_links = ('id', 'ScientificName')
    list_filter = ('scientificName',)
    list_editable = ('is_published', 'primaryCommonName')
    search_fields = ('scientificName', 'family', 'molecules', 'economicComments')
    list_per_page = 25


admin.site.register(Plants)
admin.site.register(Family)
admin.site.register(Molecules)
admin.site.register(EconomicComments)
from django.contrib import admin
from .models import *

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'is_published', 'description', 'list_date',)
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'price')
    list_per_page = 25


admin.site.register(Products, ProductAdmin)
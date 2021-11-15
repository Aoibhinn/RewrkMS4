from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Products


@admin.register(Products)
class ProductAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('product_title',)}
    list_display = ('product_title', 'slug', 'status', 'created_on')
    search_fields = ['product_title', 'description']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')

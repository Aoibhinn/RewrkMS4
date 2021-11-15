from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import Service


@admin.register(Service)

class Service(SummernoteModelAdmin):


    prepopulated_fields = {'slug': ('service_name',)}
    list_display = ('service_name', 'slug', 'status', 'created_on')
    search_fields = ['service_name', 'description']
    list_filter = ('status', 'created_on')
    summernote_fields = ('description')

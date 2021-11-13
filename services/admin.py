from django.contrib import admin

from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_title', 'price', 'is_published')
    list_filter = ('plan',)
    list_editable = ('is_published',)
    search_fields = ('service_title', 'service_description')
    list_per_page = 6


admin.site.register(Service, ServiceAdmin)

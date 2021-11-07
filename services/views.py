from django.shortcuts import render
from django.views import generic 
from . models import Service

class ServiceList(generic.ListView):
    model = Service
    # queryset = service.objects.filter(is_published=True)
    template_name = 'services.html'
    paginate_by = 6




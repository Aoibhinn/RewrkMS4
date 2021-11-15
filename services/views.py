from django.views import generic, View
from .models import Service
from django.shortcuts import render

class ServiceList(generic.ListView):
    model = Service
    queryset = Service.objects.filter(status=1)
    template_name = 'services.html'

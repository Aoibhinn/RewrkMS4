from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, DetailView, ListView
from django.shortcuts import render
from django.views import generic
from . models import Service

class ServiceList(generic.ListView):
    template_name = 'services.html'
    queryset = Service.objects.filter(is_published=True)
    context_object_name = "services"
    paginate_by = 6


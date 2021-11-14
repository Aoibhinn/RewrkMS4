from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import DetailView, ListView
from django.views import generic
from .models import Service

class ServiceList(generic.ListView):
    template_name = 'services.html'
    queryset = Service.objects.filter(is_published=True)
    context_object_name = "services"
    paginate_by = 6

def ServiceDetail(request, slug):
    queryset = Service.objects.filter(is_published=True)
    service = get_object_or_404(Service, slug=slug)

    context = {
        'service': service
    }

    return render(request, 'service.html', context)
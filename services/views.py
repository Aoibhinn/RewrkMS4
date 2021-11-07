from django.shortcuts import render
from django .views import generic
from .models import Service

Class ServiceList(generic.ListView):
    model = Service
    queryset = Course.objects.order_by('plan').filter(is_published=True)
    context_object_name = "services"
    paginate_by = 6



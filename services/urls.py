from . import views
from django.urls import path 

urlpatterns = [
    path('services', views.ServiceList.as_view(), name='services')
]
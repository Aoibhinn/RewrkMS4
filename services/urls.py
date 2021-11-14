from . import views
from django.urls import path
from services.views import ServiceDetail


urlpatterns = [
    path('services/', views.ServiceList.as_view(), name='services'),
    path('<slug:slug>/', ServiceDetail, name='service_detail'),
]
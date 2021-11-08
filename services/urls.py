from . import views
from django.urls import path



urlpatterns = [
    path('services', views.ServiceList.as_view(), name='services_urls'),
    # path('<int:pk>/', views.ServiceDetailView.as_view(), name='service'),
]
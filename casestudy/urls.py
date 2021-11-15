from . import views
from django.urls import path

urlpatterns = [
    path('casestudy/', views.PostList.as_view(), name='casestudy'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('<str:product_name>/', views.product_detail_by_name, name='product_detail_by_name'),
]
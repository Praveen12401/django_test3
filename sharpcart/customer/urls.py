from django.urls import path
from . import views

urlpatterns = [
    path('', views.customer_home, name='customer_home'),
    path('register/', views.register, name='register'),
    path('customer_orders/', views.customer_orders, name='customer_orders'),
]
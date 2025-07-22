from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product/list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product/detail.html', {'product': product})

def product_detail_by_name(request, product_name):
    product = get_object_or_404(Product, name=product_name)
    return render(request, 'product/detail.html', {'product': product})
from django.shortcuts import render
from . import views
from .models import Category, Product

# Create your views here.
# def index(request):
#     return render(request, 'store/index.html')
def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/home.html', {'products': products})

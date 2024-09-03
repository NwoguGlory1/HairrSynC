from django.shortcuts import render
from . import views
from .models import Category, CategoryImage, Product

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def home(request):
    return render(request, 'store/home.html')

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/all-products.html', {'products': products})

def signup(request):
    return render(request, 'store/signup.html')

def login(request):
    return render(request, 'store/login.html')

def logout(request):
    return render(request, 'store/logout.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/check-out.html')
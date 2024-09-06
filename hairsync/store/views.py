from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
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
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('store/home.html')
    else:
        form = UserCreationForm()
    return render(request, 'store/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('store/home.html')
    else:
        form = AuthenticationForm()

    return render(request, 'store/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'store/index.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/check-out.html')
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import views

from .models import Category, CategoryImage, Product

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def home(request):
    return render(request, 'store/home.html')

# def categories(request):
#     return {
#         'categories': Category.objects.all()
#     }

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/all-products.html', {'products': products})

def double_drawn(request, slug):
    return render(request, 'store/doubledrawn.html')

def signup(request):
    # Check if the HTTP request method is POST (form submission)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
         
        # Check if a user with the provided username already exists
        user = User.objects.filter(username=username)
         
        if user.exists():
            # Display an information message if the username is taken
            messages.info(request, "Username already taken!")
            return redirect('/signup/')
         
        # Create a new User object with the provided information
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username
        )
         
        # Set the user's password and save the user object
        user.set_password(password)
        user.save()
         
        # Display an information message indicating successful account creation
        messages.info(request, "Account created Successfully!")
        return redirect('/signup/')
     
    # Render the registration page template (GET request)
    return render(request, 'store/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return redirect('/login/')

        # Authenticate the user  with the provided username, password
        user = authenticate(username=username, password=password)
        
        # Check if authentication was successful
        if user is None:
            # Display an error message if authentication fails (invalid password)
            messages.error(request, "Invalid Password")
            return redirect('/login/')
        else:
            # Log in the user and redirect to the home page upon successful login
            login(request, user)
            return redirect('/home/')
    else:
        return render(request, 'store/login.html')

def logout_view(request):
    logout(request)
    return render(request, 'store/index.html')

def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/check-out.html')
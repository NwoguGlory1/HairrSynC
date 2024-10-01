from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import views
from .forms import SignUpForm
from .forms import EmailValidationOnForgotPassword
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from .forms import EmailValidationOnForgotPassword
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView
from django.contrib.auth.decorators import login_required

from .models import Category, CategoryImage, Product

# Create your views here.
def index(request):
    return render(request, 'store/index.html')

def home(request):
    return render(request, 'store/home.html')

def category_products(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug) #Gets all info about category
    # products = Product.objects.filter(category=category) used if you have category field in product model
    products = Product.objects.filter(categories=category) # cause you used plural categories
    return render(request, 'store/category_products.html', {'category': category, 'products': products})

def all_products(request):
    products = Product.objects.all()
    return render(request, 'store/all-products.html', {'products': products})

def detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'store/detail.html', {'product': product})

def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        
        # First check if the form is valid before additional checks
        if form.is_valid():
            email = form.cleaned_data.get('email')
            
            # Check if the email already exists
            if User.objects.filter(email=email).exists():
                messages.error(request, 'The email you inputted is already in use')
            else:
                # If the email is unique, save the user and log them in
                user = form.save(commit=False)

                # Add the first name, last name, and email before saving
                user.first_name = form.cleaned_data.get('first_name')
                user.last_name = form.cleaned_data.get('last_name')
                user.email = email

                # Now save the user to the database
                user.save()
                
                login(request, user)
                messages.success(request, "Account created successfully!")
                return redirect('/login/')
        else:
            # If the form is not valid (other field errors like username or password)
            messages.error(request, "Username already exists!")

        return render(request, 'store/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'store/signup.html', {'form': form})

    # Check if the HTTP request method is POST (form submission)
    # if request.method == 'POST':
    #     first_name = request.POST.get('first_name')
    #     last_name = request.POST.get('last_name')
    #     username = request.POST.get('username')
    #     password = request.POST.get('password')
         
    #     # Check if a user with the provided username already exists
    #     user = User.objects.filter(username=username)
         
    #     if user.exists():
    #         # Display an information message if the username is taken
    #         messages.error(request, "Username already taken!")
    #         return redirect('/signup/')
         
    #     # Create a new User object with the provided information
    #     user = User.objects.create_user(
    #         first_name=first_name,
    #         last_name=last_name,
    #         username=username
    #     )
         
    #     # Set the user's password and save the user object
    #     user.set_password(password)
    #     user.save()
         
    #     # Display an information message indicating successful account creation
    #     messages.info(request, "Account created Successfully!")
    #     return redirect('/login/')
    #     #  return redirect('login')
     
    # # Render the registration page template (GET request)
    # return render(request, 'store/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if a user with the provided username exists
        if not User.objects.filter(username=username).exists():
            # Display an error message if the username does not exist
            messages.error(request, 'Invalid Username')
            return render(request, 'store/login.html')

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
    

class CustomPasswordResetView(PasswordResetView):
    template_name = 'store/password_reset_form.html'  # Template to render when the user accesses the password reset form.
    form_class = EmailValidationOnForgotPassword  # override Django's default form and instruct it to use your custom form instead.
    success_url = reverse_lazy('password_reset_done')  # Redirect on success

    # Optional: Add form invalid handling to display errors
    # def form_invalid(self, form):
    #     return self.render_to_response(self.get_context_data(form=form))

    def form_valid(self, form):
        # Get the email from the cleaned form data (this will be validated by the form's clean_email method)
        email = form.cleaned_data.get('email')

        # Store the email in the session
        self.request.session['email'] = email

        # Proceed with the rest of the password reset process
        return super().form_valid(form)

# Handles the "Password Link Sent" page
class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'store/password_reset_done.html'  # Template for "Password Link Sent" page

    def get_context_data(self, **kwargs):
        # Call the parent class to get the default context
        context = super().get_context_data(**kwargs)

        # Retrieve the email from the session (if it exists)
        email = self.request.session.get('email', '')

        # Add the email to the context so it can be displayed in the template
        context['email'] = email

        return context

def logout_view(request):
    logout(request)
    return render(request, 'store/index.html')

@login_required
def userprofile_view(request):
    return render(request, 'store/userprofile.html', {
        'user': request.user,  # Pass the user object to the template
    })


def cart(request):
    return render(request, 'store/cart.html')

def checkout(request):
    return render(request, 'store/check-out.html')
# store/forms.py
# from django import forms


# class SignupForm(forms.Form):
#     username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
#     first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
#     last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
#     email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
#     password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
#     confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password'}))

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User  # Assuming you have a custom User model

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)
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
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms.widgets import EmailInput, PasswordInput

class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Username',
                }), 
            'first_name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'First name',
                }), 
            'last_name': forms.TextInput(attrs={
                        'class':'form-control',
                        'placeholder':'Last name',
                }),
            'email': EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email adress'}),
        }
        # password1 and password2 are declare on the UserCreationForm (they aren't model fields), therefore you can't use them in widgets
        def __init__(self, *args, **kwargs):
            super(SignUpForm, self).__init__(*args, **kwargs)
            self.fields['email'].widget = forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email address'})
            self.fields['password1'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
            self.fields['password2'].widget = PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password confirmation'})
            
class EmailValidationOnForgotPassword(PasswordResetForm):
    def clean_email(self):
        email = self.cleaned_data.get('email')
        print(f"Validating email: {email}")  # Added this to check if email was retrieved by outputting it to terminal
        if not User.objects.filter(email__iexact=email, is_active=True).exists():
            raise ValidationError("There is no user registered with the specified email address!")
        return email
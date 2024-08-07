# from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# User model user registration, login, logout, and password & profile management. Useful for tracking customer information, order history, and preferences.
# class User(AbstractUser):
#     # All fields below are already taken care of and the commented fields are taken care of too 
#     pass  # Use pass to indicate that this is a placeholder for future code

# Product model
# Category model
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='subcategories')
    image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    def __str__(self):
        return self.name
# Order model
# Cart model
# from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
# User model user registration, login, logout, and password & profile management. Useful for tracking customer information, order history, and preferences.
# class User(AbstractUser):
#     # All fields below are already taken care of and the commented fields are taken care of too 
#     pass  # Use pass to indicate that this is a placeholder for future code

# Category model
class Category(models.Model):
    #id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256, unique=True)
    #name = models.CharField(max_length=256, db_index=True) db_index makes search faster by creating a databse 
    slug = models.SlugField(max_length=255, unique=True, null=True)
    #later, manually update the slug for each product through  djangoadmin & remove null=True once all slugs are populated.)
    #slug is to include searches like http://127.0.0.1:8000/django/, makes urls friendly
    description = models.TextField(blank=True, null=True)
    #parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='subcategories')
    #image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'
        #overrides django from saying categorys on admin

    def __str__(self):
        return self.name


class CategoryImage(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='category_images/')
    
    def __str__(self):
        return self.name


# Product model
class Product(models.Model):
   id = models.AutoField(primary_key=True)
   name = models.CharField(max_length=255)
   description = models.TextField(blank=True, null=True)
   slug = models.SlugField(max_length=255, unique=True, null=True)
   #later, manually update the slug for each product through  djangoadmin & remove null=True once all slugs are populated.
   image = models.ImageField(upload_to='images/', blank=True, null=True)
   price = models.DecimalField(max_digits=10, decimal_places=2)
#    created = models.DateTimeField(auto_now_add=True)
#    updated = models.DateTimeField(auto_now=True)
   categories = models.ManyToManyField('Category')
#  category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='products')

class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created')
        def __str__(self):
            return self.name

# Order model
# Cart model
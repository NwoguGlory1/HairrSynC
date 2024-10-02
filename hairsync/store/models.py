# from django.contrib.auth.models import AbstractUser
from django.db import models
import datetime
from django.urls import reverse
from django.contrib.auth.models import User, AbstractUser

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
    #description = models.TextField(blank=True, null=True)
    #parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.SET_NULL, related_name='subcategories')
    #image = models.ImageField(upload_to='category_images/', blank=True, null=True)

    class Meta:
        verbose_name_plural = 'categories'
        #overrides django from saying categorys on admin
    
    @staticmethod
    def get_all_categories(): 
        return Category.objects.all() 

    def get_absolute_url(self):
        # used to build '<slug:slug>/' url 
        return reverse('detail', args=[self.slug])
    
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
    description = models.TextField(blank=True, null=False, default="Default description")
    slug = models.SlugField(max_length=255, unique=True, null=True)
    # later, manually update the slug for each product through django admin & remove null=True once all slugs are populated.
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ManyToManyField('Category')
    # many to many is because a single product can belong to multiple categories.
    # category = models.ForeignKey('Category', on_delete=models.SET_NULL, related_name='products')

    class Meta:
        verbose_name_plural = 'Products'
        # ordering = ('-created',)

    def get_absolute_url(self):
        # used to build '<slug:slug>/' url 
        return reverse('detail', args=[self.slug])

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    def __str__(self):
        return self.name

# Customer model
class Customer(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)   

# to save the data 
    def register(self): 
        self.save() 
    
    @staticmethod
    def get_customer_by_email(email): 
        try: 
            return Customer.objects.get(email=email) 
        except: 
            return False
  
    def isExists(self): 
        if Customer.objects.filter(email=self.email): 
            return True
  
        return False

# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True, max_length=254, verbose_name='email address')
    
#     def __str__(self):
#         return self.username
# Order model
class Order(models.Model): 
    products = models.ManyToManyField('Product')  
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE) 
    quantity = models.IntegerField(default=1) 
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=50, default='', blank=True) 
    phone = models.CharField(max_length=50, default='', blank=True) 
    date = models.DateField(default=datetime.datetime.today) 
    status = models.BooleanField(default=False) 

    def placeOrder(self): 
        self.save() 
  
    @staticmethod
    def get_orders_by_customer(customer_id): 
        return Order.objects.filter(customer=customer_id).order_by('-date') 

# Extending User Model Using a One-To-One Link
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='profile_pics') #default='default.jpg' is the default image to use for a user if they don't upload one 
    #The second argument upload_to='profile_images' is the directory where images get uploaded to

    bio = models.TextField() #The bio is just a text field where some information about users is stored

    def __str__(self):
        return self.user.username
    # return f"{self.user.username}'s profile"

# Cart model
class CartItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'
# Payment model

# ShippingAddress model
class ShippingAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address1 = models.CharField("Address1", max_length=1024)
    address2 = models.CharField("Address2", max_length=1024, blank=True, null=True)
    city = models.CharField("City", max_length=1024)
    postal_code = models.CharField("POSTAL", max_length=12)
    country = models.CharField(max_length=100)
    zip_code = models.CharField("ZIP", max_length=12)
    date_added = models.DateTimeField(auto_now_add=True)

# Review model
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField(blank=True, null=True)

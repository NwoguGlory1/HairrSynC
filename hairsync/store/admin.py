from django.contrib import admin
from .models import Category, Profile, Product, CategoryImage, CartItem, ShippingAddress, Review

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    # Display these fields in the list view of the admin
    list_display = ['user', 'avatar', 'bio']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity']
    # list_filter = ['user', 'created_at']
    # search_fields = ['product__name', 'user__username']

@admin.register(ShippingAddress)
class ShippingAddressAdmin(admin.ModelAdmin):
    list_display = ['user', 'address1', 'address2', 'city', 'postal_code', 'country', 'date_added']
    list_filter = ['country', 'city', 'address1', 'address2']
    search_fields = ['user']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'rating', 'comment']
    list_filter = ['user', 'rating']
    search_fields = ['user', 'product']
from django.contrib import admin
from .models import Category, Product, CategoryImage

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(CategoryImage)
class CategoryImageAdmin(admin.ModelAdmin):
     list_display = ['name', 'image']
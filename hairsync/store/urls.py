from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

app_name = "store"
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('all-products/', views.all_products, name='all_products'),
] 
from django.urls import path
from . import views
#from django.contrib.auth import views as auth_views

# app_name = "store"
urlpatterns = [
    # Home Page
    path('', views.index, name='index'),
    
    path('home/', views.home, name='home'),
    
    path('all-products/', views.all_products, name='all_products'),
    
    path('item/<slug:slug>/', views.detail, name='detail'),
    # path('', views., name=''),

    path('category/<slug:category_slug>/', views.category_products, name='category_products'),

    path('signup/', views.signup, name='signup'), 
    path('login/', views.login_view, name='login'), 
    path('logout/', views.logout_view, name='logout'), 

    path('cart/', views.cart, name='cart'),
    # path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    #path('cart', auth_middleware(Cart.as_view()), name='cart'), 
    path('check-out/', views.checkout, name='check-out'), 
    #path('orders', auth_middleware(OrderView.as_view()), name='orders'), 
] 
from django.urls import path
from . import views
from .views import CustomPasswordResetView, CustomPasswordResetDoneView 
from django.contrib.auth import views as auth_views

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

    # Forgot password URL
    # path('password_reset/', auth_views.PasswordResetView.as_view(template_name='store/password_reset_form.html'), name='password_reset'),
    
    # Forgot password URL (using the custom view)
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    # Page shown after submitting email for password reset
     path('password-reset/done/', CustomPasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='store/password_reset_done.html'), name='password_reset_done'),
    # URL from the password reset email for the user to enter a new password
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='store/password_reset_confirm.html'), name='password_reset_confirm'),
    # Page shown after the user successfully resets their password
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='store/password_reset_complete.html'), name='password_reset_complete'),
    
    path('logout/', views.logout_view, name='logout'), 

    path('userprofile/', views.userprofile_view, name='userprofile'),     

    path('edit-profile/', views.editprofile_view, name='edit-profile'),     


    path('cart/', views.cart, name='cart'),
    # path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    # path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    #path('cart', auth_middleware(Cart.as_view()), name='cart'), 
    path('check-out/', views.checkout, name='check-out'), 
    #path('orders', auth_middleware(OrderView.as_view()), name='orders'), 
] 
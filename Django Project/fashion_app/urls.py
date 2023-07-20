"""
URL configuration for man_fashion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('register/',views.register,name='register'),
   path('login/',views.login,name='login'),
   path('otp/',views.otp,name="otp"),
   path('logout/', views.logout, name='logout'),
   path('profile/', views.profile, name='profile'),
   path('shop/', views.shop, name='shop'),
   path('Error/', views.Error, name='Error'),
   path('shop_details/<int:pk>', views.shop_details, name='shop_details'),
   path('shopping_cart/<int:pk>', views.shopping_cart, name='shopping_cart'),
   path('cart/', views.cart, name='cart'),
   path('delete_cart/<int:pk>', views.delete_cart, name='delete_cart'),
   path('update_cart/', views.update_cart, name='update_cart'),
   path('search/', views.search, name='search'),
   path('checkout/', views.checkout, name='checkout'),
   path('checkout_details/paymenthandler/', views.checkout_details, name='checkout_details'),
   path('checkout_details/paymenthandler/paymenthandler/', views.payment, name='payment'),
   path('Categories/<str:pk>', views.Categories, name='Categories'),
   path('Categories_B/<str:pk>', views.Categories_B, name='Categories_B'),
   path('Categories_P/<str:pk>', views.Categories_P, name='Categories_P'),
   path('Categories_S/<str:pk>', views.Categories_S, name='Categories_S'),
   path('Categories_C/<str:pk>', views.Categories_C, name='Categories_C'),
   path('Categories_T/<str:pk>', views.Categories_T, name='Categories_T'),
   path('my_order', views.my_order, name='my_order'),
   path('contact', views.contact, name='contact'),
   path('about_us', views.about_us, name='about_us'),
   path('blog', views.blog, name='blog'),

]

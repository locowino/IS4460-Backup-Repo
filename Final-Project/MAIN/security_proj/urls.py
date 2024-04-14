
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from customer import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('customer.urls')),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(next_page= '/accounts/login/'), name = 'logout'),
    path('shopping-cart/', views.shopping_cart, name='shopping_cart'),
    path('movie-list/', views.movies_list, name='movie-list'),
    path('shopping-cart/checkout/', views.checkout, name= 'checkout'),
    
    #customer/main/movie-list.html
]



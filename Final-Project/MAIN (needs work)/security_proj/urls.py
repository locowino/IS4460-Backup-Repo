
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('customer.urls')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(next_page= '/accounts/login/'), name = 'logout'),
    
]


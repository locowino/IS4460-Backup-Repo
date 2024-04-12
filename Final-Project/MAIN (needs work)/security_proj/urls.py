
from django.contrib import admin
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.http import HttpResponse

def movie_list(request):
    return HttpResponse("This is the movies list page.")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/',include('customer.urls')),
    path('movies/', movie_list, name='movie-list'),

    path("accounts/", include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(next_page= '/accounts/login/'), name = 'logout'),
]


from django.urls import path
from .views import CustomerListView
from . import views

urlpatterns = [
    path('main/',CustomerListView.as_view(),name='main_page'),
    path('movies/', views.movies_list, name='movies-list'),
    
]
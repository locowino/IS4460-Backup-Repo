from django.urls import path
from .views import CustomerListView
from . import views

urlpatterns = [
    path('main/',CustomerListView.as_view(),name='main_page'), 
    path('place-order/', views.place_order, name = 'place_order'),   
    path('movie-request', views.movie_request, name = 'movie_request'),
]

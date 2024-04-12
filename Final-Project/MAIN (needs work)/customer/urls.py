from django.urls import path
from .views import CustomerListView
from . import views

urlpatterns = [
    path('main/',CustomerListView.as_view(),name='main_page'),    
]

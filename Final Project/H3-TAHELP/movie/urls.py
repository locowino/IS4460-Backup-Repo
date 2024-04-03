from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.MovieList.as_view(), name='Movie-list'),
    path('details/<int:id>/', views.MovieDetail.as_view(), name='Movie-details'),
    path('edit/<int:id>/', views.MovieEdit.as_view(), name='Movie-edit'),
    path('delete/<int:id>/', views.MovieDelete.as_view(), name='Movie-delete'),
    path('add/', views.MovieAdd.as_view(), name='movie-add'),
    path('create_api/', views.MovieListCreateView.as_view(),name='Movie-list-create'),
    path('detail_api/<int:pk>/', views.MovieDetailView.as_view(),name='movie-detail-api')
]
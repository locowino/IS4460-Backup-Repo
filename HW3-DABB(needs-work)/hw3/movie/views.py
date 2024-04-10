from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Movie
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import generics
from django.urls import reverse
from .forms import MovieForm
from .serializers import MovieSerializer
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView


def login_view(request):
    form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def customer_list(request):
    customers = [...]  # Your customer data
    user_message = "Welcome to the Customer List!"
    return render(request, 'customer_list.html', {'customers': customers, 'user_message': user_message})


# Create your views here.
class MovieList(View):
    def get(self,request):
        movies = Movie.objects.all()
        return render(request = request,template_name = 'movies/movie-list.html',context = {'movies':movies})
    

class MovieDetails(View):
    def get(self,request,movie_id=None):
        if movie_id:
            movie = Movie.objects.get(pk=movie_id)
        else:
            movie = Movie()

        movie_form = MovieForm(instance=movie)

        for field in movie_form.fields:
            movie_form.fields[field].widget.attrs['disabled'] = True
        return render(request = request,template_name = 'movies/movie-details.html',context = {'movie':movie,'movie_form':movie_form})
    
    def post(self,request,movie_id=None):
        return redirect(reverse("movie-list"))

class MovieAdd(View):

    def get(self,request):
        movie_form = MovieForm()
        return render(request = request,template_name = 'movies/movie-add.html',context = {'movie_form':movie_form})
    
    def post(self,request):
        movie_form = MovieForm(request.POST)

        if movie_form.is_valid():
            movie = movie_form.save()
        return render(request = request,template_name = 'movies/movie-add.html',context = {'movie':movie,'movie_form':movie_form})
    
    
class MovieUpdateView(UpdateView):
    model = Movie
    fields = ['title', 'description', 'director', 'release_year', 'budget', 'runtime', 'rating', 'genre']
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('movie-list')


class MovieDeleteView(View):
    def get(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        return render(request, 'movies/movie-delete.html', {'movie': movie})

    def post(self, request, movie_id):
        movie = get_object_or_404(Movie, pk=movie_id)
        movie.delete()
        return redirect('movie-list')
    

class MovieListCreateView(generics.ListCreateAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
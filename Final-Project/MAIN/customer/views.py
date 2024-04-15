from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Customer, Order, movieRequest, Movie
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

#for movie
from rest_framework import generics
from django.urls import reverse
from .forms import MovieForm
from .serializers import MovieSerializer
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView


# Create your class based views here.

class CustomerListView(LoginRequiredMixin, View):

    def get(self,request):
        main_pages = Customer.objects.all()
        return render(request=request,
                      template_name='main_page/main_page.html',
                      context = {'main_pages':main_pages}
                      )

def movies_list(request):
    return render(request, 'movies/movie-list.html')

def shopping_cart(request):
    return render(request, 'shopping_cart/shopping_cart.html')

def checkout(request):
    return render(request, 'shopping_cart/checkout.html')

def place_order(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment')
        
        # Save the form data to the database
        Order.objects.create(name=name, email=email, address=address, payment_method=payment_method)
        
        # Redirect to a success page or any other page you want
        return HttpResponseRedirect('/customer/main/') 
    else:
        # Handle GET request if needed
        pass


def movie_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comments = request.POST.get('comments')
  
        
        # Save the form data to the database
        movieRequest.objects.create(name=name, email=email, comments = comments)
        return HttpResponseRedirect('/customer/main/') 
    else:
        pass
       
# Created movie views here.
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
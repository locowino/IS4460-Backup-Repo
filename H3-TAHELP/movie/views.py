from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Movie
from django.views import View
from .forms import MovieForm
from rest_framework import generics
from .serializers import MovieSerializer


# Create your views here.
class MovieList(View):

    def get(self,request):

        movies = Movie.objects.all()

        return render(request = request,template_name = 'Movie/movie_list.html',context = {'movies':movies})

class MovieDetail(View):

    def get(self,request,id):

        movie = Movie.objects.get(pk=id)

        return render(request=request, template_name='Movie/movie_details.html',context={'movie':movie})
    
class MovieEdit(View):

    def get(self,request,id):

        movie = Movie.objects.get(pk=id)
        form = MovieForm(instance=movie)

        return render(request = request,template_name = 'Movie/movie_edit.html',context = {'Movie':movie,'form':form})
    
    def post(self,request,id):

        movie = Movie.objects.get(pk=id)
        form = MovieForm(request.POST,instance=movie)

        if form.is_valid():
            movie = form.save()
            return redirect('Movie-details', id=id)
        
        return render(request = request,template_name = 'Movie/movie_edit.html',context = {'Movie':movie,'form':form})

class MovieDelete(View):

    def get(self,request,id):

        if id:
            movie = Movie.objects.get(pk=id)
        else:
            movie = Movie()

    
        form = MovieForm(instance=movie)

        for field in form.fields:
            form.fields[field].widget.attrs['disabled'] = True

        return render(request = request,template_name = 'Movie/movie_delete.html',context = {'Movie':movie,'form':form})
      
    
    def post(self,request,id):

        movie = Movie.objects.get(pk=id)

        form = MovieForm(request.POST,instance=movie)

        movie.delete()

        return redirect(reverse("Movie-list"))

class MovieAdd(View):
    def get(self, request):
        form = MovieForm()
        return render(request=request, template_name='Movie/movie_add.html', context={'form': form})

    def post(self, request):
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('Movie-list'))
        else:
            return render(request=request, template_name='Movie/movie_add.html', context={'form': form})

class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

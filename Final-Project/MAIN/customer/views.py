from django.shortcuts import render
from django.views import View
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin

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
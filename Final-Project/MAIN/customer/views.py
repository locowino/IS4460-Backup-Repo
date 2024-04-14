from django.shortcuts import render
from django.views import View
from .models import Customer, Order, movieRequest
from django.http import HttpResponseRedirect
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
       

from django.shortcuts import render
from django.views import View
from .models import Main
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your class based views here.

class CustomerListView(LoginRequiredMixin, View):

    def get(self,request):
        main_page = Main.objects.all()
        return render(request=request,
                      template_name='main_page/main_page.html',
                      context = {'main_page':main_page}
                      )

def movies_list(request):
    return render(request, 'templates/movies/movies-list.html')
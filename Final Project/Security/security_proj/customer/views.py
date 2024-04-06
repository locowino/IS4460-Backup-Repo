from django.shortcuts import render
from django.views import View
from .models import Customer
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your class based views here.

class CustomerListView(LoginRequiredMixin, View):

    def get(self,request):
        customers = Customer.objects.all()
        return render(request=request,
                      template_name='customer/customer_list.html',
                      context = {'customers':customers}
                      )

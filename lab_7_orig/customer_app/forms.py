from django import forms
from customer_app.models import Customer,Order,Contact

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'  

    
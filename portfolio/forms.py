from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone')
        
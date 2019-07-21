from django import forms
from django.contrib.auth.models import User
from .models import Customer, Stock, Investment

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('customer_number', 'name', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone')
        
class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ('customer', 'symbol', 'name', 'shares', 'purchase_price', 'purchase_date')

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ('customer', 'category', 'description', 'acquired_value', 'acquired_date')
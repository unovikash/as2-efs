from django import forms
from .models import Customer, Stock, Investment

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
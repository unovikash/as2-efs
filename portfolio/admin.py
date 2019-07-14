from django.contrib import admin
from .models import Customer, Investment, Stock

# Register your models here.
class CustomerList(admin.ModelAdmin):
    list_display = ('customer_number', 'name', 'city', 'cell_phone')
    list_filter = ('city',)
    search_fields = ('customer_number', 'name', 'email')
    ordering = ['customer_number']

class InvestmentList(admin.ModelAdmin):
    list_display = ('customer', 'category', 'description', 'recent_value')
    list_filter = ('category',)
    search_fields = ('customer', 'category')
    ordering = ['customer']

class StockList(admin.ModelAdmin):
    list_display = ('customer','symbol', 'name', 'shares', 'purchase_price')
    list_filter = ('symbol', 'name')
    search_fields = ('customer','symbol', 'name')
    ordering = ['customer']

admin.site.register(Customer, CustomerList)
admin.site.register(Investment, InvestmentList)
admin.site.register(Stock, StockList)
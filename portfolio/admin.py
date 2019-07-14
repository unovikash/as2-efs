from django.contrib import admin
from .models import Customer

# Register your models here.
class CustomerList(admin.ModelAdmin):
    list_display = ('customer_number', 'name', 'city', 'cell_phone')
    list_filter = ('city',)
    search_fields = ('customer_number', 'name', 'email')
    ordering = ['customer_number']

admin.site.register(Customer, CustomerList)
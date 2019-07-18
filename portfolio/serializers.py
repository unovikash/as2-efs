from rest_framework import serializers
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
            model = Customer
            fields = ('name', 'address', 'customer_number', 'city', 'state', 'zipcode', 'email', 'cell_phone')

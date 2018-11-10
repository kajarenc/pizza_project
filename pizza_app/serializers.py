from rest_framework import serializers
from pizza_app.models import Pizza, Customer, Order

class PizzaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class CustomerOrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer()
    pizza = PizzaSerializer()

    class Meta:
        model = Order
        fields = '__all__'

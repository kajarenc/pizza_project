from rest_framework import serializers
from pizza_app.models import Pizza, Customer, Order

class PizzaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pizza
        fields = '__all__'


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

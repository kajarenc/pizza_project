from django.shortcuts import render
from rest_framework import viewsets
from pizza_app.models import Pizza, Customer, Order
from pizza_app.serializers import PizzaSerializer, CustomerSerializer, OrderSerializer

# Create your views here.

class PizzaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer

class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
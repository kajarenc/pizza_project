from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from pizza_app.models import Pizza, Customer, Order
from pizza_app.serializers import PizzaSerializer, CustomerSerializer, OrderSerializer, CustomerOrderSerializer

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

    @action(detail=True, methods=['get'])
    def orders(self, request, pk=None):
        queryset = Order.objects.filter(customer=pk)
        serializer = CustomerOrderSerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)
        

class OrderViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pizza_app.models import Pizza, Customer, Order

class PizzaTests(APITestCase):
    def test_create_pizza(self):
        """
        Ensure we can create a new pizza object.
        """
        url = reverse('pizzas-list')
        data = {'name': 'Quattro Formaggio'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Pizza.objects.count(), 1)
        self.assertEqual(Pizza.objects.get().name, 'Quattro Formaggio')

class CustomerTests(APITestCase):
    def setUp(self):
        self.pizza_name = 'Pepperoni'
        self.customer_first_name = 'John'
        self.customer_last_name = 'Galt'
        self.customer_email = 'john.galt@gmail.com'
    
    def test_create_customer(self):
        """
        Ensure we can create a new customer object.
        """
        url = reverse('customers-list')
        data = {
            'first_name': 'John',
            'last_name': 'Galt',
            'email': 'john.galt@gmail.com'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 1)
        self.assertEqual(Customer.objects.get().first_name, 'John')
    
    def test_customer_order(self):
        pizza = Pizza.objects.create(name=self.pizza_name)
        customer = Customer.objects.create(
            first_name=self.customer_first_name,
            last_name=self.customer_last_name,
            email=self.customer_email
        )
        url = reverse('orders-list')

        data = {
            'customer': customer.id,
            'pizza': pizza.id,
            'size': 'small'
        }
        response = self.client.post(url, data, format='json')
        order_id = response.data['id']

        url = reverse('customers-detail', args=[customer.id]) + 'orders/'

        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['pizza']['name'], self.pizza_name)

class OrderTests(APITestCase):
    def setUp(self):
        self.pizza_name = 'Pepperoni'
        self.customer_first_name = 'John'
        self.customer_last_name = 'Galt'
        self.customer_email = 'john.galt@gmail.com'

    
    def test_create_order(self):
        pizza = Pizza.objects.create(name=self.pizza_name)
        customer = Customer.objects.create(
            first_name=self.customer_first_name,
            last_name=self.customer_last_name,
            email=self.customer_email
        )
        url = reverse('orders-list')
        data = {
            'customer': customer.id,
            'pizza': pizza.id,
            'size': 'small'
        }
        response = self.client.post(url, data, format='json')
        id = response.data['id']
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get(id=id).pizza.name, self.pizza_name)






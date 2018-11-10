from django.test import TestCase

# Create your tests here.
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from pizza_app.models import Pizza

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
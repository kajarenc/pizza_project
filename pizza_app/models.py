from django.db import models

# Create your models here.

class Customer(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return '{0} {1} [{2}]'.format(
            self.first_name,
            self.last_name,
            self.email
            )


class Pizza(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Order(models.Model):
   PIZZA_SIZES = (
       ('small', 30),
       ('large', 50)
   )
   pizza = models.ForeignKey(Pizza, null=True, on_delete=models.SET_NULL)
   customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
   size = models.CharField(max_length=5, choices=PIZZA_SIZES)
   address = models.CharField(max_length=256, default='Moscow, Russia')

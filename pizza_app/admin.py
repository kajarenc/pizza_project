from django.contrib import admin

from pizza_app.models import Pizza, Customer, Order

admin.site.register(Pizza)
admin.site.register(Customer)
admin.site.register(Order)


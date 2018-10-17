from django.contrib import admin
from . import models


@admin.register(models.logins)
class Login(admin.ModelAdmin):
    list_display = ['id', 'username', 'customer_id']


@admin.register(models.customers)
class Customer(admin.ModelAdmin):
    list_display = ['id', 'forename', 'surname', 'add1', 'add2', 'add3', 'postcode', 'email', 'registered']


@admin.register(models.orders)
class Order(admin.ModelAdmin):
    list_display = ['id', 'customer_id', 'registered', 'delivery_add_id', 'payment_type', 'date', 'status', 'session', 'total']


@admin.register(models.delivery_addresses)
class Delivery_address(admin.ModelAdmin):
    list_display = ['id', 'forename', 'surname', 'add1', 'add2', 'add3', 'postcode', 'phone', 'email']


@admin.register(models.order_items)
class Order_item(admin.ModelAdmin):
    list_display = ['id', 'order_id', 'product_id', 'quantity']


@admin.register(models.products)
class Product(admin.ModelAdmin):
    list_display = ['id', 'cat_id', 'name', 'description', 'image', 'price']


@admin.register(models.categories)
class Category(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'image']
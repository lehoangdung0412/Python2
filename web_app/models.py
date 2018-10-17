from django.db import models


class customers(models.Model):
    id = models.AutoField(primary_key=True)
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100, blank=True, null=True)
    add3 = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.IntegerField()
    email = models.EmailField(max_length=254)
    registered = models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.surname, self.forename)


class logins(models.Model):
    id = models.AutoField(primary_key=True)
    customer_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)


class delivery_addresses(models.Model):
    id = models.AutoField(primary_key=True)
    forename = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    add1 = models.CharField(max_length=100)
    add2 = models.CharField(max_length=100, blank=True, null=True)
    add3 = models.CharField(max_length=100, blank=True, null=True)
    postcode = models.IntegerField()
    phone = models.IntegerField()
    email = models.EmailField(max_length=254)


class orders(models.Model):
    id = models.AutoField(primary_key=True)
    customers_id = models.ForeignKey(customers, on_delete=models.CASCADE)
    registered = models.BooleanField(default=False)
    delivery_add_id = models.ForeignKey(delivery_addresses, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=20)
    date = models.DateTimeField('date order')
    status = models.BooleanField(default=False)
    session = models.CharField(max_length=20, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)


class categories(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(blank=True, verbose_name='Post categories')


class products(models.Model):
    id = models.AutoField(primary_key=True)
    cat_id = models.ForeignKey(categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, verbose_name='Post product')
    price = models.DecimalField(max_digits=10, decimal_places=2)


class order_items(models.Model):
    id = models.AutoField(primary_key=True)
    other_id = models.ForeignKey(orders, on_delete=models.CASCADE,)
    product_id = models.ForeignKey(products, on_delete=models.CASCADE,)
    quantity = models.IntegerField()





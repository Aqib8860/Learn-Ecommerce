from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customerss', null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return str(self.user)


class Product(models.Model):
    pass
    CATEGORY = (
        ('Fashion', 'Fashion'),
        ('Mobile', 'Mobile'),
        ('Electronics', 'Electronics'),
        ('Home', 'Home'),
        ('Appliances', 'Appliances'),
        ('Sports', 'Sports'),
        ('Books', 'Books'),
        ('Furniture', 'Furniture'),
    )
    added_by = models.ForeignKey('auth.user', related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)
    image = models.ImageField(null=True, blank=False)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('Delivered', 'Delivered'),
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
    )
    # customer = models.ForeignKey(Customers, related_name='orders', on_delete=models.SET_NULL, blank=True, null=True)
    customer = models.ForeignKey('auth.user', related_name='orders', on_delete=models.CASCADE, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return str(self.customer)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)

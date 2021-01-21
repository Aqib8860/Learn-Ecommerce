from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.PrimaryKeyRelatedField(many=True, queryset=Product.objects.all())
    # products = serializers.HyperlinkedModelSerializer(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'last_login', 'products']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    added_by = serializers.ReadOnlyField(source='added_by.username')

    class Meta:
        model = Product
        fields = ['url', 'name', 'price', 'image', 'category', 'added_by']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    customer = serializers.ReadOnlyField(source='customer.username')
    # url = serializers.HyperlinkedIdentityField(view_name="user")

    class Meta:
        model = Order
        fields = '__all__'

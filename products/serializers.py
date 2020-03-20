from rest_framework import serializers
from .models import Product
from django.contrib.auth.models import User


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ['url', 'id', 'name', 'category', 'owner']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    products = serializers.HyperlinkedRelatedField(many=True, view_name='product-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'username', 'email', "first_name", "last_name", "products"]


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', "password", 'email', "first_name", "last_name"]

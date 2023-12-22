from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = StringRelatedField()
    category = StringRelatedField()
    class Meta:
        model = Category
        fields = '__all__'

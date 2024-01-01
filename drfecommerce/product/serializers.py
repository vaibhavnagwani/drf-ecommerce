from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Category, ProductLine, Product, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class ProductLineSerializer(serializers.ModelSerializer):
    # product = ProductSerializer()
    class Meta:
        model = ProductLine
        exclude = ['id', 'product', 'is_active']


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(source='brand.name')
    category_name = serializers.CharField(source='category.name')
    product_name = serializers.CharField(source='name')
    product_lines = ProductLineSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'brand_name', 'category_name', 'product_name', 'product_lines', 'slug', 'description', 'is_digital']
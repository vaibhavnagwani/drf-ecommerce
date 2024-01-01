from rest_framework import serializers
from rest_framework.relations import StringRelatedField

<<<<<<< HEAD
from .models import Category
=======
from .models import Category, ProductLine, Product, Brand, ProductImage
>>>>>>> 6a062daa5fc9ba6266d142c252f0542330cc6262


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


<<<<<<< HEAD
=======
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['name', 'url']


class ProductLineSerializer(serializers.ModelSerializer):
    product_image = ProductImageSerializer(many=True)

    class Meta:
        model = ProductLine
        fields = ['price', 'sku', 'stock_quantity', 'product_image']


>>>>>>> 6a062daa5fc9ba6266d142c252f0542330cc6262
class ProductSerializer(serializers.ModelSerializer):
    brand = StringRelatedField()
    category = StringRelatedField()
    class Meta:
<<<<<<< HEAD
        model = Category
        fields = '__all__'
=======
        model = Product
        fields = ['id', 'brand_name', 'category_name', 'product_name', 'product_lines', 'slug', 'description',
                  'is_digital']
>>>>>>> 6a062daa5fc9ba6266d142c252f0542330cc6262

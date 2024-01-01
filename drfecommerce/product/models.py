from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey("self", on_delete=models.PROTECT, null=True, blank=True, related_name="children")

    class MPTTMeta:
        order_insertion_by = ["name"]

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    category = TreeForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True, related_name="products"
    )

    def __str__(self):
        return self.name
<<<<<<< HEAD
=======


class ProductLine(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    sku = models.CharField(max_length=100)
    stock_quantity = models.PositiveIntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_lines")
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.product.name} ({self.price})'


class ProductImage(models.Model):
    name = models.CharField(max_length=100)
    alternative_text = models.CharField(max_length=100)
    url = models.ImageField(default="test.jpg")
    product = models.ForeignKey(ProductLine, on_delete=models.PROTECT, related_name="product_image")

    def __str__(self):
        return self.name
>>>>>>> 6a062daa5fc9ba6266d142c252f0542330cc6262

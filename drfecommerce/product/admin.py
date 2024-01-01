from django.contrib import admin

from .models import Category, Brand, Product, ProductLine


class ProductLineInline(admin.TabularInline):
    model = ProductLine


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductLineInline
    ]


# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ProductLine)

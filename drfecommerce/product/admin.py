from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

<<<<<<< HEAD
from .models import Category, Brand, Product
=======
from .models import Category, Brand, Product, ProductLine, ProductImage


class EditLinkInline(object):
    def edit(self, instance):
        url = reverse(
            f"admin:{instance._meta.app_label}_{instance._meta.model_name}_change", args=[instance.pk]
        )
        if instance.pk:
            link = mark_safe('<a href="{u}">edit</a>'.format(u=url))
            return link
        else:
            return ""


class ProductImageInline(admin.TabularInline):
    model = ProductImage


class ProductLineInline(EditLinkInline, admin.TabularInline):
    model = ProductLine
    readonly_fields = ("edit",)


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductLineInline
    ]

>>>>>>> 6a062daa5fc9ba6266d142c252f0542330cc6262

class ProductLineAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline
    ]


# Register your models here.
admin.site.register(ProductLine, ProductLineAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
<<<<<<< HEAD
admin.site.register(Product)
=======
>>>>>>> 6a062daa5fc9ba6266d142c252f0542330cc6262

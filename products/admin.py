from django.contrib import admin
from .models import Product, MultipleProductImages, ProductAttrs


# Register your models here.

admin.site.register(Product)
admin.site.register(ProductAttrs)
admin.site.register(MultipleProductImages)

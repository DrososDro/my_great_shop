from django.db import models
import uuid
from products.models import Product


class VariationsCategory(models.Model):
    """here is the  variation_category
    i do it this way:
        the shop admin can add variation_categories for the products
        different products have other variations
        and can add what is the needs of the shop

    """

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id = models.UUIDField(
        default=uuid.uuid4(),
        unique=True,
        primary_key=True,
        editable=False,
    )
    varation_name = models.CharField(
        max_length=200,
        unique=True,
        null=True,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Variations(models.Model):
    """each variation can have different price_b2b and different price
    can be active or not and can have their discount
    also if price here is set to zero the price is the default of the product
    the discount is in present (%)

    """

    id = models.UUIDField(
        default=uuid.uuid4(),
        unique=True,
        primary_key=True,
        editable=False,
    )
    variation_category = models.ForeignKey(
        VariationsCategory,
        on_delete=models.CASCADE,
    )
    variation_value = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(Default=True)

    price = models.FloatField(default=0, null=True, blank=True)
    price_b2b = models.FloatField(default=0, null=True, blank=True)
    discount = models.IntegerField(defautl=0, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

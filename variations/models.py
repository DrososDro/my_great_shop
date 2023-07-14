from django.db import models
import uuid
from products.models import Product


VARIATION_CHOICES = (
    ("color", "Color"),
    ("size", "Size"),
    ("material", "Material"),
    ("contition", "Contition"),
    ("product_origin", "Product Origin"),
)


class VariationsCategory(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, choices=VARIATION_CHOICES)

    def __str__(self):
        return self.name


class Variations(models.Model):
    """each variation can have different price_b2b and different price
    can be active or not and can have their discount
    also if price here is set to zero the price is the default of the product
    the discount is in present (%)

    """

    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    variation_category = models.ForeignKey(
        VariationsCategory,
        on_delete=models.CASCADE,
    )
    variation_value = models.CharField(max_length=200)
    """

    is_active = models.BooleanField(default=True)

    price = models.FloatField(default=0, null=True, blank=True)
    price_b2b = models.FloatField(default=0, null=True, blank=True)
    discount = models.IntegerField(default=0, null=True, blank=True)

    """

    class Meta:
        unique_together = [["variation_category", "variation_value"]]

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.variation_value

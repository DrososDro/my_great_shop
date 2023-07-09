from django.db import models
import uuid
from products.models import Product
from variations.models import Variations


class ProductAttrs(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, editable=False, unique=True, primary_key=True
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(
        Variations,
        on_delete=models.CASCADE,
        related_name="color",
        blank=True,
        null=True,
    )
    size = models.ForeignKey(
        Variations,
        on_delete=models.CASCADE,
        related_name="size",
        blank=True,
        null=True,
    )
    condition = models.ForeignKey(
        Variations,
        on_delete=models.CASCADE,
        related_name="condition",
        blank=True,
        null=True,
    )
    material = models.ForeignKey(
        Variations,
        on_delete=models.CASCADE,
        related_name="material",
        blank=True,
        null=True,
    )
    product_origin = models.ForeignKey(
        Variations,
        on_delete=models.CASCADE,
        related_name="product_origin",
        blank=True,
        null=True,
    )
    # quantity and price
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    price_b2b = models.FloatField(default=0)
    is_available = models.BooleanField(default=False)
    # offer
    offer_duration = models.DateTimeField(null=True, blank=True, default=0)
    offer_discount = models.IntegerField(null=True, blank=True, default=0)
    discount = models.IntegerField(default=0)

    # package dimensions in mm
    weight = models.IntegerField(default=0, null=True, blank=True)
    height = models.IntegerField(default=0, null=True, blank=True)
    width = models.IntegerField(default=0, null=True, blank=True)
    depth = models.IntegerField(default=0, null=True, blank=True)


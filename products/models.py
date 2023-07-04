import uuid
from django.db import models
from django.utils import timezone


# Create your models here.


class Product(models.Model):
    # description of product
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    product_id = models.CharField(
        max_length=200,
    )
    alternative_product_ids = models.CharField(
        max_length=400,
        null=True,
        blank=True,
    )
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=200, blank=True, null=True)
    # quantity and price
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    price_b2b = models.FloatField(default=0)
    is_available = models.BooleanField(default=False)
    # offer
    offer_duration = models.DateTimeField(null=True, blank=True, default=0)
    offer_discount = models.IntegerField(null=True, blank=True, default=0)
    discount = models.IntegerField(default=0)

    # rating
    total_star_ratio = models.FloatField(default=0)
    total_votes = models.IntegerField(default=0)

    # package dimensions in mm
    weight = models.IntegerField(default=0)
    height = models.IntegerField(default=0)
    width = models.IntegerField(default=0)
    depth = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_id

    def discount_price(self):
        return (
            self.price - (self.price * self.discount_offer() / 100)
            if self.discount_price
            else self.price
        )

    def discount_price_b2b(self):
        pass

    def offer_lasts(self):
        now = timezone.now()
        return (
            self.offer_duration
            if self.offer_duration and self.offer_duration > now
            else 0
        )

    def discount_offer(self):
        return self.offer_discount if self.offer_lasts else self.discount


class MultipleProductImages(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    image = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

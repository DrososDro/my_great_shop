import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from categories.models import Category


# Create your models here.


class Product(models.Model):
    # description of product
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    product_slug = models.SlugField(
        default=None, max_length=200, unique=True, null=True, blank=True
    )
    product_id = models.CharField(
        max_length=200,
    )
    alternative_product_ids = models.CharField(
        max_length=400,
        null=True,
        blank=True,
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
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
    weight = models.IntegerField(default=0, null=True, blank=True)
    height = models.IntegerField(default=0, null=True, blank=True)
    width = models.IntegerField(default=0, null=True, blank=True)
    depth = models.IntegerField(default=0, null=True, blank=True)

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

    @property
    def product_image_last(self):
        try:
            image = self.multipleproductimages_set.last().image.url or ""
        except Exception:
            image = ""
        return image

    def product_url(self):
        return reverse(
            "product",
            kwargs={
                "category_slug": self.category.category_slug,
                "product_slug": self.product_slug,
            },
        )


class MultipleProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    image = models.FileField()
    created_at = models.DateTimeField(auto_now_add=True)

    def image_url(self):
        return self.image.url or ""

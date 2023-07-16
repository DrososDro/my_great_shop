import uuid
from django.db import models
from django.urls import reverse
from django.utils import timezone
from categories.models import Category
from django.templatetags.static import static


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

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # rating
    total_star_ratio = models.FloatField(default=0)
    total_votes = models.IntegerField(default=0)

    class Meta:
        ordering = ["total_star_ratio", "created_at"]

    def __str__(self):
        return self.product_id

    @property
    def product_image_last(self):
        try:
            image = self.multipleproductimages_set.last().image.url or static(
                "default_images/404.jpg"
            )
        except Exception:
            image = static("default_images/404.jpg")
        return image

    def product_url(self):
        return reverse(
            "product",
            kwargs={
                "category_slug": self.category.category_slug,
                "product_slug": self.product_slug,
            },
        )

    def product_start_price(self):
        return self.productattrs_set.first().price

    def product_offer_duration(self):
        return self.productattrs_set.order_by("offer_duration").last().offer_duration

    def product_discount(self):
        product = self.productattrs_set.order_by("offer_discount").last()
        if product.offer_duration and product.offer_duration > timezone.now():
            return product.offer_discount


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
        return self.image.url or static("default_images/404.jpg")

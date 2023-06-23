import uuid
from django.db import models

# Create your models here.


class Product(models.Model):
    # description of product
    product_id = models.CharField(max_length=200, unique=True, primary_key=True)
    secontary_product_ids = models.CharField(max_length=400)
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    # quantity and price
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0)
    price_b2b = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    is_available = models.BooleanField(default=False)

    # this is if you make an order
    # is_ordered = models.BooleanField(defautl=False)
    variations = models.ManyToManyField("Variations")

    # dimensions
    weight = models.FloatField(default=0)
    height = models.FloatField(default=0)
    width = models.FloatField(default=0)
    depth = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_id} {self.name}"


# i want a choice field but i want to make it with a file
class Variations(models.Model):
    CHOICES_FIELS = [("size", "size"), ("variation", "variation")]
    id = models.UUIDField(
        default=uuid.uuid4(),
        unique=True,
        primary_key=True,
        editable=False,
    )
    size = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    pass

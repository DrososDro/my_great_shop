from django.db import models
import uuid
from products.models import ProductAttrs
from account.models import Account

# Create your models here.


class Cart(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null=True, blank=True)
    cart_id = models.CharField(max_length=250, blank=True, null=True)
    cart_items = models.ManyToManyField("CartItems")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CartItems(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    product = models.ForeignKey(ProductAttrs, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.product.quantity < self.quantity:
            self.quantity = self.product.quantity
        return super().save(*args, **kwargs)

from django.db import models
import uuid

from django.db.models.aggregates import Sum
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

    @property
    def cart_items_subtotal_sum(self):
        return sum({i.cart_subtotal for i in self.cart_items.all()})


class CartItems(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    cart_model = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductAttrs, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cart_product_id(self):
        return self.product.product.product_id

    @property
    def cart_item_price(self):
        descount_price, price = self.product.discount_price()
        return descount_price or price

    @property
    def cart_subtotal(self):
        return self.quantity * self.cart_item_price

    def get_url(self):
        return self.product.product.product_url()

    def cart_item_image(self):
        return self.product.product.product_image_last

    def save(self, *args, **kwargs):
        if self.product.quantity < self.quantity:
            self.quantity = self.product.quantity
        return super().save(*args, **kwargs)

from django.db import models
import uuid

from products.models import ProductAttrs
from account.models import Account
from variations.models import Variations

# Create your models here.


class Cart(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    user = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    shipping_method = models.CharField(max_length=200, blank=True, null=True)
    payment_method = models.CharField(max_length=200, blank=True, null=True)

    cart_id = models.CharField(max_length=250, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def cart_items_subtotal_sum(self):
        return sum((i.cart_subtotal for i in self.cartitems_set.all()))

    def cart_items_total(self):
        all = self.cart_items_subtotal_sum
        if self.shipping_method == "Shipping 20$":
            all += 20
        return all


class CartItems(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        primary_key=True,
        editable=False,
    )
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(ProductAttrs, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    variation = models.CharField(null=True, blank=True, max_length=400)

    @property
    def cart_var(self):
        if self.variation is None:
            variation_calc = [
                f"{k.replace('_id','')}: {Variations.objects.get(id=v).variation_value}"
                for k, v in self.product.__dict__.items()
                if v is not None
                and k
                in {
                    "color_id",
                    "size_id",
                    "material_id",
                    "contition_id",
                    "product_origin_id",
                }
            ]
            self.variation = (", ").join(variation_calc)
            self.save()
        return self.variation

    @property
    def cart_product_id(self):
        return self.product.product.product_id

    @property
    def cart_item_price(self):
        descount_price, price = self.product.discount_price()
        return descount_price or price

    @property
    def max_quantity(self):
        return self.product.quantity

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

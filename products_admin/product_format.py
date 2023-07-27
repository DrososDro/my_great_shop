from collections import namedtuple
from categories.models import Category
from django.utils.text import slugify

from products.models import Product, ProductAttrs
from variations.models import VariationsCategory, Variations


class NamedTupleInCsvFormat:
    def __init__(
        self,
        *,
        product_id=None,
        category=None,
        description=None,
        brand=None,
        product_alternative_ids=None,
        # in product_attrs
        price=None,
        quantity=None,
        price_b2b=None,
        # pass
        color=None,
        size=None,
        condition=None,
        material=None,
        product_origin=None
    ):
        self.category = category
        self.product_id = product_id
        self.alternative_product_ids = product_alternative_ids
        self.description = description
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.price_b2b = price_b2b
        self.variation = {
            "color": color,
            "size": size,
            "contition": condition,
            "material": material,
            "product_origin": product_origin,
        }

    def get_category_or_create(self):
        category, created = Category.objects.get_or_create(
            name=self.category, category_slug=slugify(self.category)
        )
        return category

    def get_product_or_create(self):
        self.product, created = Product.objects.get_or_create(
            product_id=self.product_id,
            product_slug=slugify(self.product_id),
            category=self.category,
        )

        if created:
            self.product.alternative_product_ids = self.alternative_product_ids
            self.product.description = self.description
            self.product.brand = self.brand
            self.product.save()
        return self.product

    def get_variations_category_or_create(self):
        variation_pass_dict = {}
        for k, v in self.variation.items():
            if v is not None:
                variation_cat, created = VariationsCategory.objects.get_or_create(
                    product=self.product, name=k
                )
                variation, created = Variations.objects.get_or_create(
                    variation_category=variation_cat, variation_value=v
                )
                variation_pass_dict[k] = variation

        variation, created = ProductAttrs.objects.get_or_create(
            product=self.product, **variation_pass_dict, offer_duration=None
        )
        if created:
            variation.quantity = self.quantity
            variation.price = self.price
            variation.price_b2b = self.price_b2b
            variation.save()
        else:
            variation.quantity += int(self.quantity)
            variation.save()

    def __call__(self):
        try:
            self.category = self.get_category_or_create()
            self.product = self.get_product_or_create()
            self.variations = self.get_variations_category_or_create()
        except Exception as e:
             pass

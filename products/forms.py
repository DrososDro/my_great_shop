from django import forms

from products.models import Product, ProductAttrs
from variations.models import Variations


class ProductForm(forms.Form):
    def __init__(self, *args, product_slug=None, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        if product_slug:
            product = Product.objects.get(product_slug=product_slug)

            variations_dict = {}

            for var_cat in product.variationscategory_set.all():
                x = Variations.objects.filter(variation_category=var_cat)
                variations_dict[var_cat] = x

            for cat, choises in variations_dict.items():
                self.fields[cat.variation_category] = forms.ModelChoiceField(
                    queryset=choises
                )

        else:
            raise ValueError

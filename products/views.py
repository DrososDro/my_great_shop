import json
from datetime import datetime
from django.http import JsonResponse
from django.views.generic import DetailView, ListView
from products.models import Product
from products.models.product_attritubes import ProductAttrs
from products.forms import ProductForm

# Create your views here.


class Home(ListView):
    model = Product
    template_name = "products/shop3.html"


class CategoryView(Home):
    def get_queryset(self):
        return self.model.objects.filter(
            category__category_slug=self.kwargs["category_slug"],
        )


class ProductView(DetailView):
    model = Product
    template_name = "products/single_product.html"
    test = 1

    def get_object(self, queryset=None):
        return self.model.objects.get(product_slug=self.kwargs["product_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["form"] = ProductForm(product_slug=self.object.product_slug)
        return context

    def post(self, *args, **kwargs):
        self.test += 1
        print(self.test)

        data_dict = {
            i["name"]: i["value"]
            for i in json.loads(self.request.body)
            if i["value"] != ""
        }

        price = ""
        offer = ""
        offer_duration = ""
        quantity = "Out of Stock"
        discount_price = ""

        try:
            product = ProductAttrs.objects.get(
                product__product_slug=kwargs["product_slug"], **data_dict
            )
            price = f"{product.price}$"
            if product.offer_duration_():
                price_, discount_price_ = product.discount_price()

                offer_duration = (
                    f" Until {product.offer_duration.strftime('%d-%m-%Y %H:%M')}"
                )
                offer = f"{product.offer_discount}% off "
                price = f"{price_}$"
                discount_price = f"{discount_price_}$"
            if product.quantity:
                quantity = product.quantity

        except Exception:
            pass

        return JsonResponse(
            {
                "price": price,
                "offer": offer,
                "offer_duration": offer_duration,
                "quantity": quantity,
                "discount_price": discount_price,
            }
        )

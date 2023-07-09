from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView
from products.models import Product
from products.models.product_attritubes import ProductAttrs
from variations.models import Variations, VariationsCategory
from products.forms import ProductForm
from django.core import serializers

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

    def get_object(self, queryset=None):
        return self.model.objects.get(product_slug=self.kwargs["product_slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        x = self.object.variationscategory_set.all()  # .objects.variations_set.all()
        # x = self.object.productattrs_set.all()
        for i in x:
            print(i)
        print(x)
        return context


def product_view(request, category_slug, product_slug):
    product = Product.objects.get(product_slug=product_slug)
    form = ProductForm(product_slug=product_slug)
    attrs = ProductAttrs.objects.filter(product=product)
    data = serializers.serialize("json", attrs)
    attrs = JsonResponse(data, safe=False)

    context = {"object": product, "form": form, "attrs": attrs}
    return render(request, "products/single_product.html", context)

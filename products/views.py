from django.shortcuts import render
from django.views.generic import DetailView, ListView
from products.models import Product

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

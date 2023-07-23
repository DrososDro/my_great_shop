from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, ListView
from cart.models import Cart
from cart.utils import get_or_create_cart
from django.contrib import messages


# Create your views here.


class AddToCart(View):
    def post(self, *args, **kwargs):
        cart = get_or_create_cart(self.request)

        product = self.request.POST["productattr_id"]
        quantity = self.request.POST["quantity"]
        redirect_path = self.request.POST["redirect_path"]

        cart_item, created = cart.cart_items.get_or_create(product_id=product)
        if created:
            cart_item.quantity = int(quantity)
        else:
            cart_item.quantity += int(quantity)

        cart_item.save()
        messages.success(self.request, "Your item sucessfully added to cart!")
        return redirect(redirect_path)


class CartView(ListView):
    template_name = "cart/shop-cart.html"

    def get_queryset(self):
        return get_or_create_cart(self.request)

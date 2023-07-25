from django.shortcuts import redirect
from django.views import View
from django.views.generic import ListView
from cart.models import CartItems
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


class UpdateProductQuantiry(View):
    def get(self, *args, **kwargs):
        try:
            cart_item = CartItems.objects.get(id=kwargs["pk"])
        except CartItems.DoesNotExist:
            pass
        else:
            if kwargs["action"] == "+":
                cart_item.quantity += 1
            elif kwargs["action"] == "-":
                cart_item.quantity -= 1
            else:
                cart_item.quantity = 0

            if cart_item.quantity > cart_item.max_quantity:
                cart_item.quantity = cart_item.max_quantity

            cart_item.save()

            if cart_item.quantity < 1:
                cart_item.delete()
        return redirect("cart")


class CartView(ListView):
    template_name = "cart/shop-cart.html"

    def get_queryset(self):
        return get_or_create_cart(self.request)

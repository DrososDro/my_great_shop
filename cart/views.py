from django.shortcuts import redirect
from django.views import View
from cart.utils import create_cart
from django.contrib import messages


# Create your views here.


class AddToCart(View):
    def post(self, *args, **kwargs):
        cart = create_cart(self.request)

        product = self.request.POST["productattr_id"]
        quantity = self.request.POST["quantity"]

        cart_item, created = cart.cart_items.get_or_create(product_id=product)
        if created:
            cart_item.quantity = int(quantity)
        else:
            cart_item.quantity += int(quantity)

        cart_item.save()
        messages.success(self.request, "Your item sucessfully addet to cart!")
        return redirect(self.request.path)

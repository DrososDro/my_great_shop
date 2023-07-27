from django.shortcuts import redirect
from django.views import View
from django.views.generic import DetailView, ListView
from cart.models import CartItems
from cart.utils import get_billint_address, get_delivery_address, get_or_create_cart
from django.contrib import messages


# Create your views here.


class AddToCart(View):
    def post(self, *args, **kwargs):
        cart = get_or_create_cart(self.request)

        product = self.request.POST["productattr_id"]
        quantity = self.request.POST["quantity"]
        redirect_path = self.request.POST["redirect_path"]

        cart_item, created = CartItems.objects.get_or_create(
            product_id=product, cart=cart
        )
        if created:
            cart_item.quantity = int(quantity)
        else:
            cart_item.quantity += int(quantity)

        cart_item.save()
        messages.success(self.request, "Your item sucessfully added to cart!")
        return redirect(redirect_path)


class UpdateProductQuantity(View):
    def get(self, *args, **kwargs):
        try:
            CartItems.objects.get(id=kwargs["pk"]).delete()
        except CartItems.DoesNotExist:
            pass

        messages.success(self.request, "Your Cart sucessfully updated!")
        return redirect("cart")

    def post(self, *args, **kwargs):
        form_dict = self.request.POST
        for pk, value in form_dict.items():
            try:
                cart_item = CartItems.objects.get(id=pk)
                int(value)
            except Exception as e:
                pass
            else:
                cart_item.quantity = int(value)
                cart_item.save()

        messages.success(self.request, "Your Cart sucessfully updated!")
        return redirect("cart")


class CartView(DetailView):
    template_name = "cart/shop-cart.html"

    def get_object(self):
        return get_or_create_cart(self.request)

    def post(self, *args, **kwargs):
        payment = self.request.POST.get("payment_method")
        shiping = self.request.POST.get("shipping_method")
        cart = self.get_object()
        cart.shipping_method = shiping
        cart.payment_method = payment
        cart.save()

        return redirect("checkout")


class Checkout(ListView):
    template_name = "cart/shop-checkout.html"

    def get_queryset(self):
        return get_or_create_cart(self.request)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        cart = self.get_queryset()
        context["billing_address"] = get_billint_address(self.request)
        context["delivery_address"] = get_delivery_address(self.request)
        context["payment_method"] = cart.payment_method
        context["shipping_method"] = cart.shipping_method

        return context


class Test(ListView):
    template_name = "cart/shop-order-complete.html"

    def get_queryset(self):
        return None

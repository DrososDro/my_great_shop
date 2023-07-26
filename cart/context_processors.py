from django.db.models import Sum

from cart.models import Cart


def cart_items_assign(request):
    items = {}
    try:
        cart = Cart.objects.get(user=request.user)
    except Exception:
        try:
            cart = Cart.objects.get(cart_id=request.session.session_key)
        except Exception:
            cart = None
    if cart:
        items = cart.cartitems_set.aggregate(Sum("quantity"))

    return dict(cart_quantity=items.get("quantity__sum"))

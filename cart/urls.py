from django.urls import path
from cart import views


urlpatterns = [
    path("cart/", views.CartView.as_view(), name="cart"),
    path(
        "update-product/<str:pk>/",
        views.UpdateProductQuantity.as_view(),
        name="update-product",
    ),
    path("checkout/", views.Checkout.as_view(), name="checkout"),
]

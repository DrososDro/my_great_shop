from django.urls import path
from products import views
import cart.views as cart_view

urlpatterns = [
    path(
        "add-to-cart/",
        cart_view.AddToCart.as_view(),
        name="add-to-cart",
    ),
    path("", views.Home.as_view(), name="home"),
    path(
        "<slug:category_slug>/",
        views.CategoryView.as_view(),
        name="category",
    ),
    path(
        "<slug:category_slug>/<slug:product_slug>/",
        views.ProductView.as_view(),
        name="product",
    ),
]

from django.urls import path
from products import views

urlpatterns = [
    path("", views.Home.as_view(), name="home"),
    path(
        "<slug:category_slug>/",
        views.CategoryView.as_view(),
        name="category",
    ),
    path(
        "<slug:category_slug>/<slug:product_slug>/",
        views.product_view,
        name="product",
    ),
]

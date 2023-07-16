from django.urls import path
from products_admin import views

urlpatterns = [
    path(
        "csv-product-add/",
        views.add_products_with_csv,
        name="csv-product-add",
    ),
]

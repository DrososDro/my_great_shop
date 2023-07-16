from os import walk
from products.models import Product


def recent_products(request):
    return {
        "recent_products": Product.objects.all().order_by(
            "-created_at",
        )[:3],
    }


def top_rated_products(request):
    return {
        "top_rated": Product.objects.all().order_by(
            "-total_star_ratio",
            "-created_at",
        )[:3],
    }


def related_products(request, category_slug=None):
    category_slug = request.resolver_match.kwargs.get("category_slug")
    if category_slug:
        return {
            "related_products": Product.objects.filter(
                category__category_slug=category_slug,
            )[:10]
        }
    return {}

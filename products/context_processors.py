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

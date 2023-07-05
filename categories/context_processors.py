from categories.models import Category


def list_of_categories(request):
    categories = Category.objects.all()
    return dict(list_of_categories=categories)

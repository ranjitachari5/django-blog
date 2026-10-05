from .models import Category
def categories_dict(request):
    categories=Category.objects.all()
    return dict(categories=categories)
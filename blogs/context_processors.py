from django.db.models import Q

from .models import Blog, Category
def categories_dict(request):
    categories=Category.objects.all()
    return dict(categories=categories)
def search_item(request):
    keyword=request.GET.get('keyword','')
    
    if keyword:
        blog=Blog.objects.filter(
        Q(title__icontains=keyword) |
        Q(short_description__icontains=keyword)|
        Q(blog_body__icontains=keyword )|
        Q(created_at__icontains=keyword )|
        Q(updated_at__icontains=keyword ),
        status='Published')
    else:
        blog = Blog.objects.filter(status='Published')

    return dict(search_blog=blog,keyword=keyword)
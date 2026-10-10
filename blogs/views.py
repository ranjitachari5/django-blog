from django.shortcuts import get_object_or_404, render
from django.db.models import Q
from .models import Blog, Category
# Create your views here.
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(category_id=category_id,status="Published")
    category = get_object_or_404(Category, id=category_id)
    context={"posts":posts,"category":category,}
    return render(request,'post_by_category.html',context)

# single blog
def blogs(request,slug):
    single_blog=get_object_or_404(Blog ,slug=slug,status='Published')
    context={"single_blog":single_blog,}
    return render(request,'blog.html',context)

# seach feature
def search(request):
    return render(request,'search.html')
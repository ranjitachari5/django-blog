from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
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
    keyword=request.GET.get('keyword')
    blog=Blog.objects.filter(
        Q(title__icontains=keyword) |
        Q(short_description__icontains=keyword)|
        Q(blog_body__icontains=keyword ),
        status='Published')
    context={"search_blog":blog}
    return render(request,'search.html',context)
from django.http import HttpResponse
from django.shortcuts import render

from blogs.models import Blog, Category
def home(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status="Published")
    posts=Blog.objects.filter(is_featured=False,status="Published")
    context={'categories':categories,"featured_posts":featured_posts,"posts":posts,}
    return render(request,'home.html',context)
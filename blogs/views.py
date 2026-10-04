from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse

from .models import Blog, Category
# Create your views here.
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(category_id=category_id,status="Published")
    categories=Category.objects.all()
    category = get_object_or_404(Category, id=category_id)
    context={"posts":posts,"category":category,"categories":categories}
    return render(request,'post_by_category.html',context)

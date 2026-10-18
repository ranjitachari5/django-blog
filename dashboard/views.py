from django.shortcuts import get_object_or_404, redirect, render

from .forms import CategoryForm
from blogs.models import Blog, Category
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count=Category.objects.all().count() 
    blogs_count=Blog.objects.all().count()
    context={
        'category_count':category_count,
        'blogs_count':blogs_count,
    }
    return render(request,'dashboards/dashboard.html',context)

def categories(request):
    return render(request,'dashboards/categories.html')


@login_required(login_url='login')
def add_category(request):
    form=CategoryForm()
    if(request.method=="POST"):
        form=CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    context={'form':form}
    return render(request,'dashboards/add_category.html',context)




@login_required(login_url='login')
def edit_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    if request.method=='POST':

        form=CategoryForm(request.POST,instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
       form=CategoryForm(instance=category)
    context={
        'form':form,
        'category':category,
    }
    return render(request,'dashboards/edit_category.html',context)

@login_required(login_url='login')
def delete_category(request,pk):
    category=get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')
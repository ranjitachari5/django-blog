from django.shortcuts import get_object_or_404, redirect, render

from blogs.forms import RegistrationForm
from .forms import AddUserForm, BlogForm, CategoryForm, UserForm
from blogs.models import Blog, Category
from django.contrib.auth.models import User
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



@login_required
def posts(request):
    if request.user.is_superuser:
        posts = Blog.objects.all()
    else:
        posts = Blog.objects.filter(author=request.user)
    return render(request, 'dashboards/posts.html', {'posts': posts})


@login_required(login_url='login')
def delete_post(request,pk):
    blog=get_object_or_404(Blog,pk=pk)
    blog.delete()
    return redirect('posts')

@login_required(login_url='login')
def edit_post(request,pk):
    blog=get_object_or_404(Blog,pk=pk)
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES,                                               instance=blog)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('posts')
    else:
        form=BlogForm(instance=blog)
    context={'form':form}
    
    return render(request,'dashboards/edit_post.html',context)

@login_required(login_url='login')
def add_post(request):
    
    if request.method=='POST':
        form=BlogForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('posts')
        else:
            print(form.errors)

    else:
        form=BlogForm()
    context={
        'form':form
    }
    return render(request,'dashboards/add_post.html',context)

@login_required(login_url='login')
def users(request):
    users=User.objects.all()
    context={
        'users':users,
    }
    return render(request,'dashboards/users.html',context)

@login_required(login_url='login')
def edit_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    if request.method=='POST':
        form=UserForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form=UserForm(instance=user)
    context={
        'form':form
    }
    return render(request,'dashboards/edit_user.html',context)

@login_required(login_url='login')
def delete_user(request,pk):
    user=get_object_or_404(User,pk=pk)
    user.delete()
    return redirect('users')

@login_required(login_url='login')
def add_user(request):
    if request.method=='POST':
        form=AddUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form=AddUserForm()
    context={'form':form}
    return render(request,'dashboards/add_user.html',context)

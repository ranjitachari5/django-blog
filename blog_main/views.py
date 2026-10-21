from django.http import HttpResponse
from django.shortcuts import redirect, render
from blogs.forms import RegistrationForm
from blogs.models import Blog, Category
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import Group, User
def home(request):
    categories=Category.objects.all()
    featured_posts=Blog.objects.filter(is_featured=True,status="Published")
    posts=Blog.objects.filter(is_featured=False,status="Published")
    context={'categories':categories,"featured_posts":featured_posts,"posts":posts,}
    return render(request,'home.html',context)
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        username=request.POST.get('username')
        users=User.objects.filter(username=username)
        if users:
            print("User Exists")
        if form.is_valid():
            user=form.save() 
            editor_group = Group.objects.get(name='Editor')
            user.groups.add(editor_group)
            return redirect('login') 
        else:
            print(form.errors)
    else:
        form=RegistrationForm()
    context={'form':form}
    return render(request,'register.html',context)
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {"form": form})
def logout(request):
    auth.logout(request)
    return redirect('home')
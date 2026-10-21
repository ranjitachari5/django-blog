from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.core.exceptions import PermissionDenied

from blogs.forms import CommentForm
from .models import Blog, Category, Comment
# Create your views here.
def posts_by_category(request,category_id):
    posts=Blog.objects.filter(category_id=category_id,status="Published")
    category = get_object_or_404(Category, id=category_id)
    context={"posts":posts,"category":category,}
    return render(request,'post_by_category.html',context)

# single blog

def blogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='Published')

    if request.method == 'POST':
        # comments require login
        if not request.user.is_authenticated:
            return redirect('login')

        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = single_blog
            comment.user = request.user
            comment.save()
            return redirect('blog', slug=slug)
        messages.error(request, "Comment can't be empty.")

    comments = Comment.objects.filter(blog=single_blog).select_related('user')
    context = {
        "single_blog": single_blog,
        "comments": comments,
        "comments_count": comments.count(),
    }
    return render(request, 'blog.html', context)

@login_required(login_url='login')
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk, user=request.user)
    slug = comment.blog.slug
    is_owner = comment.user == request.user
    can_moderate = request.user.has_perm('blogs.delete_comment')
    if not (is_owner or can_moderate):
        raise PermissionDenied
    if request.method == "POST":
        comment.delete()

    return redirect("blog", slug=slug)
     
     



# seach feature
def search(request):
    
    return render(request,'search.html')
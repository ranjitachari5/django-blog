from django import forms
from blogs.models import Blog, Category

class CategoryForm(forms.ModelForm):
    class  Meta:
        model=Category
        fields='__all__'

class BlogForm(forms.ModelForm):
    class  Meta:
        model=Blog
        fields='__all__'
        
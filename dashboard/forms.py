from django import forms
from blogs.models import Blog, Category
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
    class  Meta:
        model=Category
        fields='__all__'

class BlogForm(forms.ModelForm):
    class  Meta:
        model=Blog
        fields='__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username", "email", "first_name", "last_name", "is_staff","is_active", "groups","user_permissions"]

class AddUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username", "email", "first_name", "last_name","is_active", "is_staff", "groups","user_permissions"]
        
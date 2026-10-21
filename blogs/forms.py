from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models

from blogs.models import Comment

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    terms = forms.BooleanField(
        required=True,
        error_messages={"required": "Please accept the terms to continue."},
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['comment']
        
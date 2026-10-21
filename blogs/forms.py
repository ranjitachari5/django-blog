from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    terms = forms.BooleanField(
        required=True,
        error_messages={"required": "Please accept the terms to continue."},
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2",)
        
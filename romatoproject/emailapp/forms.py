from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import CustomUser


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "First name")
    last_name = forms.CharField(label = "last name")

    class Meta:
        model = CustomUser
        fields = ('email','first_name','last_name' )

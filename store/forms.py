from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm


class UserSignupForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class AddProductForm(ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

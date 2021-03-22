from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views import generic
from .forms import UserLoginForm
import requests

# from django.views.generic.edit import FormView

# Create your views here.


class Home(generic.ListView):
    template_name = 'apistore/product_list.html'
    queryset = ''


def home(request):
    return render(request, 'product_list.html')


def login_page(request):
    form = UserLoginForm

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('e-commerce:home')
            else:
                messages.info(request, 'Username or Password Incorrect')

    return render(request, 'apistore/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('e-commerce:user-login')


def my_orders2(headers, request):
    url = 'http://127.0.0.1:8000/apistoreorder-list'
    response = requests.post(url, headers=headers)
    user_orders = response.json()
    context = {
        'user_orders': user_orders
    }
    return render(request, 'apistore/myorders.html', context)


def my_orders(request):
    return render(request, 'apistore/myorders.html')

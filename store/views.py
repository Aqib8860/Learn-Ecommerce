from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import *


def register(request):
    form = UserSignupForm

    if request.method == 'POST':
        form = UserSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account successfully created for' + username)
            return redirect('store:login')

    context = {'form': form}
    return render(request, 'register.html', context)


def login_page(request):
    form = UserLoginForm
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('api_store:home')
        else:
            messages.info(request, 'Username or Password Incorrect')
    context = {'form': form}
    return render(request, 'login.html', context)


def user_logout(request):
    logout(request)
    return redirect('store:login')


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)


def cart(request):
    context = {}
    return render(request, 'cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'checkout.html', context)


def my_orders(request):
    customer = request.user.customer
    orders = Order.objects.filter(customer=customer)
    orders_delivered = orders.filter(status='Delivered').count()
    orders_pending = orders.filter(status='Pending').count()

    order = Order.objects.filter(customer=customer)
    items = OrderItem.objects.filter(order__id__in=order.all())
    context = {
        'orders': orders,
        'orders_delivered': orders_delivered,
        'orders_pending': orders_pending,
        'items': items,
    }
    return render(request, 'myorders.html', context)


def add_product(request):
    form = AddProductForm

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product Successfully Add')
            return redirect('store:add_product')
    context = {'form': form}
    return render(request, 'add_product.html', context)

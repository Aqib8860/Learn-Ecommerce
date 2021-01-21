from django.urls import path
from . import views


app_name = 'store'
urlpatterns = [
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('my_orders/', views.my_orders, name='my_orders'),
    path('add_product/', views.add_product, name='add_product'),
]

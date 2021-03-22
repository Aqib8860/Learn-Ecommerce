from django.urls import path
from . import views


app_name = 'e-commerce'
urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('user-login/', views.login_page, name='user-login'),
    path('user-logout/', views.user_logout, name='user-logout'),
    path('my-orders/', views.my_orders, name='my-orders'),

]

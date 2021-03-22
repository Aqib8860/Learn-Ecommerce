from django.urls import path
from . import views


urlpatterns = [
    path('', views.api_root, name='api-root'),
    path('user-list', views.UserList.as_view(), name='user-list'),
    path('user/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('product-list', views.ProductList.as_view(), name='product-list'),
    path('product-detail/<int:pk>/', views.ProductDetail.as_view(), name='product-detail'),
    path('order-list', views.OrderList.as_view(), name='order-list'),
    path('order-detail/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('orderitem-list', views.OrderItemList.as_view(), name='orderitem-list'),
    path('orderitem-detail/<int:pk>', views.OrderItemDetail.as_view(), name='orderitem-detail'),
    path('allorder-list', views.AllOrderList.as_view(), name='allorder-list'),
    path('allorder-detail/<int:pk>', views.AllOrderDetail.as_view(), name='allorder-detail'),
]

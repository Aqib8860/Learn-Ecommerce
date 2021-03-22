from rest_framework.decorators import api_view, APIView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics, permissions, status
from .serializers import *
from .models import Product
from .permissions import IsOwnerOrReadOnly
# from django.shortcuts import get_object_or_404

# Create your views here.


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
        'orderitems': reverse('orderitem-list', request=request, format=format),
        'allorders': reverse('allorder-list', request=request, format=format),
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        serializer.save(added_by=self.request.user)


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]


class AllOrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = AllOrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllOrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = AllOrdersSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        user = request.user
        orders = Order.objects.filter(customer=user)
        # items = OrderItem.objects.filter(order__id__in=orders.all())
        serializer_context = {
            'request': request,
        }
        serializer = OrderSerializer(orders, many=True, context=serializer_context)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderDetailSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated]

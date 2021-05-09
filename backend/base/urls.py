from django.urls import path
from . import views

urlpatterns = [
    path('users/login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/profile/', views.getUserProfile, name="users-profile"),
    path('users/profile/update/', views.updateUserProfile, name="users-profile-update"),
    path('users/register/', views.registerUser, name='register'),
    path('products/', views.getProducts, name="products"),
    path('products/top/', views.getTopProducts, name='top-products'),
    path('products/<str:pk>/', views.getProduct, name="product"),
    path('users/', views.getUsers, name="users"),
    path('orders/add/', views.addOrderItems, name="orders-add"),
    path('orders/myorders/', views.getMyOrders, name="myorders"),
    path('orders/<str:pk>/deliver/', views.updateOrderToDelivered, name='order-delivered'),
    path('orders/<str:pk>/', views.getOrderById, name="user-order"),
    path('orders/<str:pk>/pay/', views.updateOrderToPaid, name="pay"),
]

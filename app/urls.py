from django.urls import path,include

from app.views import CategroyListApiView, ProductListApiView, \
    ProductUpdateAPIView, ProductDestroyAPIView, UserRegistration

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)




urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh'),
    path('category/list',CategroyListApiView.as_view(), name='list_category'),
    path('product/list', ProductListApiView.as_view(), name='product_category'),
    path('product/update/<pk>', ProductUpdateAPIView.as_view(), name='product_update'),
    path('product/delete/<pk>', ProductDestroyAPIView.as_view(), name='product_destroy'),
    path('register/', UserRegistration.as_view(), name='user-registration'),
]
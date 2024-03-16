from django_filters.rest_framework import DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
from rest_framework import generics, status
from rest_framework import permissions
from rest_framework.authtoken.admin import User
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from app.models import Categroy, Product
from app.permissions import IsOwnerOrReadOnly
from app.serializer import CategoryModelSerializer, ProductUpdateDeleteModelSerializer, ProductModelSerializer,UserRegisterModelSerializer
from django.conf import settings
from django.core.mail import send_mail
class CategroyListApiView(ListAPIView):
    queryset = Categroy.objects.all()
    serializer_class = CategoryModelSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('name',)
    pagination_class = PageNumberPagination



class ProductListApiView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductModelSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name', 'description',)
    pagination_class = PageNumberPagination


class ProductUpdateAPIView(UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductUpdateDeleteModelSerializer

class ProductDestroyAPIView(DestroyAPIView):
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductUpdateDeleteModelSerializer

class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterModelSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        email_subject = 'Ro\'yxatdan o\'tdingiz'
        email_message = 'Siz muvaffaqiyatli ro\'yxatdan o\'tdingiz.'
        send_mail(email_subject, email_message, settings.EMAIL_HOST_USER, [user.email])
        return Response({'message': 'Foydalanuvchi ro\'yxatdan o\'tdi va xabar yuborildi.'}, status=status.HTTP_201_CREATED)

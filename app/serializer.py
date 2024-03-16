from app.models import User
from rest_framework.serializers import ModelSerializer,ValidationError,CharField

from app.models import Categroy, Product


class CategoryModelSerializer(ModelSerializer):
    class Meta:
        model = Categroy
        fields = ('name',)


class ProductModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name',)


class ProductUpdateDeleteModelSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'categroy',)

class UserRegisterModelSerializer(ModelSerializer):
    password_confirm = CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise ValidationError("Parollar mos kelmadi")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
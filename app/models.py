import uuid
from django.db.models import Model, CharField, TextField, ForeignKey, ImageField,DateTimeField, DO_NOTHING, CASCADE,UUIDField
from django.contrib.auth.models import AbstractUser



# Create your models here.
class User(AbstractUser):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)

class Categroy(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(max_length=255)

class Product(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    name = CharField(max_length=255)
    description = TextField()
    owner = ForeignKey(User, on_delete=CASCADE)
    categroy = ForeignKey(Categroy, on_delete=DO_NOTHING)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Image(Model):
    uuid = UUIDField(primary_key=True, default=uuid.uuid4)
    product = ForeignKey(Product, on_delete=CASCADE)
    image = ImageField(upload_to='user/')

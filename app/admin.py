from django.contrib.admin import ModelAdmin
from django.contrib import admin
from app.models import Categroy,Product


# Register your models here.
@admin.register(Categroy)
class ChatModelAdmin(ModelAdmin):
    ist_display = 'name'


@admin.register(Product)
class ProductModelAdmin(ModelAdmin):
    ist_display = 'name','category'

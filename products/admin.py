from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_filter = ('id', 'name')
    search_fields = ('id', 'name')
    list_per_page = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'name', 'description', 'price', 'quantity', 'image', 'category')
    list_filter = ('id', 'name', 'price', 'category')
    search_fields = ('id', 'name', 'price', 'category')
    list_per_page = 10



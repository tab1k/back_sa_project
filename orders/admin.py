from django.contrib import admin

from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','buyer', 'product', 'quantity', 'total_price', 'date_ordered')
    list_filter = ('buyer', 'product', 'quantity')
    search_fields = ('buyer', 'product', 'quantity','total_price', 'date_ordered')
    list_per_page = 10


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'product', 'rating', 'comment')
    list_filter = ('id', 'product', 'rating', 'comment')
    search_fields = ('id','user', 'product', 'rating','comment')
    list_per_page = 10

@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user','product')
    list_filter = ('id', 'product')
    search_fields = ('id', 'user', 'product')
    list_per_page = 10


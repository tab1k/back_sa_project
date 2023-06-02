from django.contrib import admin

from .models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'date_joined', 'is_active', 'is_seller')
    list_filter = ('id', 'date_joined', 'is_active', 'is_seller')
    search_fields = ('id', 'date_joined', 'is_active', 'is_seller')
    list_per_page = 10


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'name', 'address', 'phone_number')
    list_filter = ('id', 'user', 'name', 'address', 'phone_number')
    search_fields = ('id', 'user', 'name', 'address', 'phone_number')
    list_per_page = 10
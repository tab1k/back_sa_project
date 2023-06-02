from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class User(AbstractUser):
    # Поля по умолчанию из AbstractUser
    # username
    # password
    # email
    # first_name
    # last_name

    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_seller = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group, related_name='users_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='users_set', blank=True)


class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='company')
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

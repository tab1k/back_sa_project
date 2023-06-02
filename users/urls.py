from .views import *
from django.urls import path


app_name = 'users'

urlpatterns = [
    path('signin/', RegistrationView.as_view(), name='signin'),
    path('login/', LoginView.as_view(), name='login')
]

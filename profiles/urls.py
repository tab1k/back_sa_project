from django.urls import path
from .views import UserProfileView

app_name = 'profiles'

urlpatterns = [
    path('user_profile/', UserProfileView.as_view(), name='user_profile'),
    # Дополнительные маршруты для профилей пользователей
]
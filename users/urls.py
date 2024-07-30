from django.urls import path

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('users/', UserListAPIView.as_view(), name='users_list'),
    path('users/create/', UserCreateAPIView.as_view(), name='users_create'),
]

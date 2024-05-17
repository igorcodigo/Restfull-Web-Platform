# myapp/urls.py

from django.urls import path
from .views import UserCreateView, UserListView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/register/', UserCreateView.as_view(), name='user-register'),
]

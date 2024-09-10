from django.urls import path
from .views import *

urlpatterns = [
    path('users/register/', UserRegisterGenericView.as_view(), name='user register'),
    path('users/', UserListGenericView.as_view(), name='user list'),
]
from django.urls import path
from .views import *

urlpatterns = [
    path('users/register/', UserRegisterGenericView.as_view(), name='user-register'),
    path('users/', UserListGenericView.as_view(), name='user-list'),
    path('users/<int:pk>', UserAdminRetrieveUpdateDestroyGenericView.as_view(), name='user-admin-retrieve-update-destroy'),
]
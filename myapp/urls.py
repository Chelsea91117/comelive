from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegisterGenericView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('users/', UserListGenericView.as_view(), name='user-list'),
    path('users/<int:pk>', UserRetrieveUpdateDestroyGenericView.as_view(), name='user-retrieve-update-destroy'),
    path('users/details/', UserDetailGenericView.as_view(), name='user-details'),
    path('ads/', AdListCreateGenericAPIView.as_view(), name='ads-list-create'),
]
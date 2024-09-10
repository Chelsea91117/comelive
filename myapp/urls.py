from django.urls import path, include
from .views import *

urlpatterns = [
    path('register/', UserRegisterGenericView.as_view(), name='Registration'),
]
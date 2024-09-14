from django.urls import path
from .views import *

urlpatterns = [
    path('register/', UserRegisterGenericView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('users/', UserListGenericView.as_view(), name='user-list'),
    #список пользователей для админа
    path('users/<int:pk>', UserRetrieveUpdateDestroyGenericView.as_view(), name='user-retrieve-update-destroy'),
    # изменение, удаление пользователей для админа
    path('users/details/', UserDetailGenericView.as_view(), name='user-details'),
    # изменение, удаление пользователя для текущего пользователя
    path('ads/', AdListCreateGenericAPIView.as_view(), name='ads-list-create'),
    # создание объявлений для владельцев и список для всех
    path('ads/<int:pk>', AdRetrieveUpdateDestroyGenericAPIView.as_view(), name='ads-retrieve-update-destroy'),
    # изменение, удаление объявлений для их владельцев
    path('ads/my/', UserAdListGenericAPIView.as_view(), name='user-ads-list'),
    # лист объявлений пользователя для текущего пользователя
    path('bookings/', BookingListGenericView.as_view(), name='booking-list'),
    # лист бронирований для текущего пользователя
    path('bookings/past/', PastBookingsListGenericView.as_view(), name='past-bookings-list'),
    # список прошедших бронирований для текущего пользователя
    path('bookings/active/', ActiveBookingsListGenericView.as_view(), name='active-bookings-list'),
    # список будущих бронирований для текущего пользователя
    path('bookings/new/', BookingCreateGenericAPIView.as_view(), name='booking-create'),
    # сoздание бронирования для арендатора
    path('bookings/<int:pk>/', BookingRetrieveUpdateGenericAPIView.as_view(), name='booking-update'),
    # изменение статуса объявления для владельцев и арендаторов
    path('ads/<int:ad_id>/booked/', BookedDatesListGenericAPIView.as_view(), name='property-booked-dates'),
    # лист забронированных дат для всех пользователей
]



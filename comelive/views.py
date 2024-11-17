from django.db.models import Q
from django.template.context_processors import request
from rest_framework import status, filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.utils import timezone
from comelive.models import *
from comelive.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime
from .permissions import IsLandlordOrReadOnly, IsOwnerOrReadOnly, IsRenter
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponse
from django.utils.html import format_html


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            # Используем exp для установки времени истечения куки
            access_expiry = datetime.utcfromtimestamp(access_token["exp"])
            refresh_expiry = datetime.utcfromtimestamp(refresh["exp"])

            response = Response(status=status.HTTP_200_OK)
            response.set_cookie(
                key="access_token",
                value=str(access_token),
                httponly=True,
                secure=False,  # Используйте True для HTTPS
                samesite="Lax",
                expires=access_expiry,
            )
            response.set_cookie(
                key="refresh_token",
                value=str(refresh),
                httponly=True,
                secure=False,
                samesite="Lax",
                expires=refresh_expiry,
            )
            return response
        else:
            return Response(
                {"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED
            )


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        return response


class UserRegisterGenericView(CreateAPIView):
    serializer_class = UserCreateUpdateSerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class UserListGenericView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserRetrieveUpdateDestroySerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserDetailGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = UserCreateUpdateSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def destroy(self, request, *args, **kwargs):
        # Получаем текущего пользователя
        user = self.get_object()
        self.perform_destroy(user)

        # Очистка куки
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")

        return response

    def perform_destroy(self, instance):
        instance.delete()


class AdListCreateGenericView(ListCreateAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsLandlordOrReadOnly]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    search_fields = ["title", "description"]
    filterset_fields = {
        "price": ["gte", "lte"],
        "state": ["icontains"],
        "city": ["icontains"],
        "rooms": ["gte", "lte"],
        "type": ["exact"],
    }
    ordering_fields = ["price", "created_at"]

    def get_queryset(self):
        return Ad.objects.filter(is_active=True)


class UserAdListGenericView(ListAPIView):
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(owner=self.request.user)


class AdRetrieveUpdateDestroyGenericView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsOwnerOrReadOnly]


class BookingCreateGenericView(CreateAPIView):
    serializer_class = BookingCreateSerializer
    queryset = Booking.objects.all()
    permission_classes = [IsRenter]


class BookingListGenericView(ListAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(
            Q(renter=self.request.user) | Q(landlord=self.request.user)
        )


class PastBookingsListGenericView(ListAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(
            Q(renter=self.request.user) | Q(landlord=self.request.user),
            end_date__lte=timezone.now(),
        )


class ActiveBookingsListGenericView(ListAPIView):
    serializer_class = BookingListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(
            Q(renter=self.request.user) | Q(landlord=self.request.user),
            start_date__gte=timezone.now(),
        )


class BookingRetrieveUpdateGenericView(RetrieveUpdateAPIView):
    serializer_class = BookingUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Booking.objects.filter(
            Q(renter=self.request.user) | Q(landlord=self.request.user)
        )


class BookedDatesListGenericView(ListAPIView):
    serializer_class = BookedDatesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_id")
        ad = get_object_or_404(Ad, pk=ad_id)

        return Booking.objects.filter(
            ad=ad, status__in=["Confirmed", "Pending"], end_date__gte=timezone.now()
        )


class ReviewCreateGenericView(CreateAPIView):
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()
    permission_classes = [IsRenter]


class ReviewListGenericView(ListAPIView):
    serializer_class = ReviewListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        ad_id = self.kwargs["ad_id"]
        return Review.objects.filter(ad__id=ad_id)


def welcome_view(request):
    html_content = format_html(
        """
        <html>
        <head>
            <title>Welcome to Come&Live API!</title>
        </head>
        <body>
            <h1>Welcome to Come&Live API!</h1>
            <h2>Available Paths:</h2>
            <ul>
                <li><a href="/admin/">admin/</a></li>
                <li><a href="/register/">register/</a> [name='registration']</li>
                <li><a href="/login/">login/</a> [name='login']</li>
                <li><a href="/logout/">logout/</a> [name='logout']</li>
                <li><a href="/users/">users/</a> [name='user-list']</li>
                <li><a href="/users/1/">users/&lt;int:pk&gt;/</a> [name='user-retrieve-update-destroy']</li>
                <li><a href="/users/details/">users/details/</a> [name='user-details']</li>
                <li><a href="/ads/">ads/</a> [name='ads-list-create']</li>
                <li><a href="/ads/1/">ads/&lt;int:pk&gt;/</a> [name='ads-retrieve-update-destroy']</li>
                <li><a href="/ads/my/">ads/my/</a> [name='user-ads-list']</li>
                <li><a href="/bookings/">bookings/</a> [name='booking-list']</li>
                <li><a href="/bookings/past/">bookings/past/</a> [name='past-bookings-list']</li>
                <li><a href="/bookings/active/">bookings/active/</a> [name='active-bookings-list']</li>
                <li><a href="/bookings/new/">bookings/new/</a> [name='booking-create']</li>
                <li><a href="/bookings/1/">bookings/&lt;int:pk&gt;/</a> [name='booking-update']</li>
                <li><a href="/bookings/ads/1/">bookings/ads/&lt;int:ad_id&gt;/</a> [name='property-booked-dates']</li>
                <li><a href="/reviews/1/">reviews/&lt;int:ad_id&gt;/</a> [name='ad-reviews-list']</li>
                <li><a href="/reviews/">reviews/</a> [name='review-create']</li>
            </ul>
        </body>
        </html>
    """
    )

    return HttpResponse(html_content)

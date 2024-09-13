from rest_framework import status, filters
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from myapp.models import User, Ad
from myapp.serializers import UserCreateUpdateSerializer, UserListSerializer, UserRetrieveUpdateDestroySerializer, \
    AdSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from datetime import datetime

from .filters import AdFilter
from .permissions import IsLandlordOrReadOnly, IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            # Используем exp для установки времени истечения куки
            access_expiry = datetime.utcfromtimestamp(access_token['exp'])
            refresh_expiry = datetime.utcfromtimestamp(refresh['exp'])

            response = Response(status=status.HTTP_200_OK)
            response.set_cookie(
                key='access_token',
                value=str(access_token),
                httponly=True,
                secure=False, # Используйте True для HTTPS
                samesite='Lax',
                expires=access_expiry
            )
            response.set_cookie(
                key='refresh_token',
                value=str(refresh),
                httponly=True,
                secure=False,
                samesite='Lax',
                expires=refresh_expiry
            )
            return response
        else:
            return Response({"detail": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):

    def post(self, request, *args, **kwargs):
        response = Response(status=status.HTTP_204_NO_CONTENT)
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')
        return response


class UserRegisterGenericView(CreateAPIView):
    serializer_class = UserCreateUpdateSerializer
    permission_classes = [AllowAny]

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


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
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

        return response

    def perform_destroy(self, instance):
        instance.delete()

class AdListCreateGenericAPIView(ListCreateAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsLandlordOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title', 'description']
    filterset_class = AdFilter
    ordering_fields = ['price', 'created_at']

    def get_queryset(self):
        return Ad.objects.filter(is_active=True)

class UserAdListGenericAPIView(ListAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Ad.objects.filter(owner=self.request.user)

class AdRetrieveUpdateDestroyGenericAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AdSerializer
    queryset = Ad.objects.all()
    permission_classes = [IsOwnerOrReadOnly]










from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView, ListAPIView

from myapp.models import User
from myapp.serializers import UserRegisterSerializer, UserListSerializer


class UserRegisterGenericView(CreateAPIView):
    serializer_class = UserRegisterSerializer

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class UserListGenericView(ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
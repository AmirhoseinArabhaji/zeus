from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserRegisterSerializers


class UserRegistrationAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(data={'message': 'You Registered Successfully!'}, status=status.HTTP_201_CREATED)


user_registration_serializer = UserRegistrationAPIView.as_view()

__all__ = [
    'user_registration_serializer',
]
from rest_framework import viewsets, status
from rest_framework.permissions import  IsAdminUser
from rest_framework.response import Response

from account.serializers import RegisterSerializers
from account.models import Users


class RegisterViewSet(viewsets.GenericViewSet):
    queryset = Users.objects.all()
    serializer_class = RegisterSerializers
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_create(self, serializer):
        password = serializer.validated_data.pop('password')
        account = Users(**serializer.validated_data)
        account.set_password(password)
        account.save()
        return account

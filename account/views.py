from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from account.models import Users
from account.serializers import AccountSerializer, AccountUpdateSerializer


class AccountView(viewsets.GenericViewSet):

    queryset = Users.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [IsAdminUser]

    action_serializers = {
        'list': AccountSerializer,
        'create': AccountUpdateSerializer,
    }

    def get_serializer_class(self):
        if hasattr(self, 'action_serializers'):
            if self.action in self.action_serializers:
                return self.action_serializers[self.action]
        return super().get_serializer_class()

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)


    def perform_update(self, serializer):
        return serializer.save()

    def create(self, request, *args, **kwargs):
        instance = request.user
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

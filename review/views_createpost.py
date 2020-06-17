from rest_framework import viewsets, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from review.models import Gallery
from review.serializers import AdminCreateSerializers, AdminPowerSerializers


class CreatePostViewSet (viewsets.GenericViewSet):
    queryset = Gallery.objects.all()
    serializer_class = AdminCreateSerializers
    permission_classes = [IsAdminUser]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        gallery = Gallery.objects.create(
            title=serializer.validated_data['title'],
            image=serializer.validated_data['image'],
            user_uploaded=request.user
        )

        serializer_data = AdminPowerSerializers(gallery)
        return Response(serializer_data.data, status=status.HTTP_201_CREATED)

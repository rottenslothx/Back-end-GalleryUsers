
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAdminUser


from review.models import Gallery
from review.serializers import AdminPowerSerializers


class GalleryViewSet(viewsets.GenericViewSet, ListModelMixin):
    queryset = Gallery.objects.all()
    serializer_class = AdminPowerSerializers
    permission_classes = [IsAdminUser]




from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.settings import api_settings

from review.models import Review, Gallery
from review.serializers import ReviewSerializers


class Reviews (viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializers

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gallery = None

    def initial(self, request, *args, **kwargs):
        self.gallery = Gallery.objects.filter(id=self.kwargs.get('gallery.id', -1)).first()
        if self.gallery is None:
            raise NotFound
        super().initial(request, *args, **kwargs)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)

        Review.objects.create(
            post_id=self.gallery.id,
            review_text=serializer.validated_data['review_text'],
            rating=serializer.validated_data['rating'],
            user_id=request.user.id
        )

        self.gallery.avg_rating = (self.gallery.avg_rating * self.gallery.review_count + serializer.validated_data['rating']) / (self.gallery.review_count+1)
        self.gallery.review_count += 1
        self.gallery.save(update_fields=['avg_rating', 'review_count'])

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}





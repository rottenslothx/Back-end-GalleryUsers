from django.conf.urls import url, include
from rest_framework import routers

from .views_createpost import CreatePostViewSet
from .views_gallery import GalleryViewSet
from .views_rating import Reviews

router = routers.DefaultRouter()
router.register(r'', GalleryViewSet)
router.register(r'review/(?P<gallery_id>[0-9]+)', Reviews)
router.register(r'create', CreatePostViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework_review'))
]
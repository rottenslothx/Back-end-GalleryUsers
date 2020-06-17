from django.conf.urls import url, include
from rest_framework import routers

from .views import AccountView
from .views_register import RegisterViewSet

router = routers.DefaultRouter()
router.register(r'register', RegisterViewSet)
router.register(r'', AccountView)

urlpatterns = [
    url(r'', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
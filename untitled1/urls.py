from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

# swagger
schema_view = get_schema_view(
   openapi.Info(
      title="Swagger API",
      default_version='v1.420',
      description="glhf",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('gallery/', include('review.urls')),
    url(r'^api/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]

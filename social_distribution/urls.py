"""social_distribution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0.5/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.urls import path, include
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from social_distribution import settings

schema_view = get_schema_view(
    openapi.Info(
        title="API DOCS",
        default_version='v1.0',
        description="api docs",
        terms_of_service="#",
        contact=openapi.Contact(email="jery"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)
from stream.api_views import *
from django.contrib import admin
from rest_framework import routers
from django.urls import re_path

router = routers.DefaultRouter()

urlpatterns = [
                  path('admin/', admin.site.urls),
                  # path('docs/swagger/', schema_view),
                  path('api/', include('stream.api_urls')),
                  path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

                  # setting drf_yasg
                  re_path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0),
                          name='schema-json'),
                  path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
                  path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

                  path('', include("home.urls", namespace="home")),
                  path('stream/', include("stream.urls", namespace="stream")),
                  path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL,
                                                                                         document_root=settings.STATIC_ROOT)

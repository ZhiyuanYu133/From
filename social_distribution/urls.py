"""social_distribution URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)

from stream import views as stream_views
from stream.models import Post, Comment
from users import views as user_views
from users.models import AuthUser


# Author API
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['type', 'id', "uuid", 'host', 'displayName', 'url', 'github', 'profileImage']


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = AuthUser.objects.all()
    serializer_class = AuthorSerializer


# Comment API
class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Comment
        fields = ['type', 'author', 'comment', 'contentType', 'published', 'id']


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


# Post API
class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(required=False)
    comments = CommentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = (
        'id', 'author', 'title', 'source', 'origin', 'contentType', 'content', 'categories', 'count', 'comments',
        'published', 'visibility', 'unlisted')

    def create(self, validated_data):
        author_data = validated_data.pop('author')
        author, _ = AuthUser.objects.get_or_create(**author_data)
        post = Post.objects.create(author=author, **validated_data)
        return post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# API router
router = routers.DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("register/", user_views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(template_name="users/logout.html"), name="logout"),
    path('profile/<uuid:id>/', user_views.profile, name='profile'),
    path('profile/edit/', user_views.profile_edit, name="profile_edit"),
    path("api/", include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # JWT, API Endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/posts/', stream_views.posts),
    path('api/posts/<uuid:id>/', stream_views.post),

    # Keep this at the bottom
    path("", include('stream.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

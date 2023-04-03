import uuid

from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils import timezone

from home.models import User


class Posts(models.Model):
    class Meta:
        ordering = ["-published"]

    id = models.IntegerField(primary_key=True, editable=False)
    type = models.CharField(max_length=255, default="post", editable=False)
    uuid = models.CharField(max_length=255, default=str(uuid.uuid4()), editable=True, unique=True)
    title = models.CharField(max_length=100)
    source = models.CharField(max_length=100, null=True)
    origin = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    contentType = models.CharField(max_length=150, blank=True, null=True)
    content = models.TextField()  # TextField can have more than 255 characters
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    categories = models.CharField(max_length=50, blank=True, null=True)
    view_count = models.BigIntegerField(default=0, null=True)
    like_count = models.BigIntegerField(default=0, null=True)
    comment_count = models.BigIntegerField(default=0, null=True)
    published = models.DateTimeField(default=timezone.now, null=True)
    image = models.ImageField(upload_to="uploads/post_photo", blank=True, null=True)
    visibility = models.CharField(max_length=150, blank=True, null=True)
    unlisted = models.BooleanField(default=False, null=True)
    is_public = models.BooleanField(default=False)
    CommonMark = models.BooleanField(default=False)
    is_friends_public = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"{self.author}"
            f"{self.id}"
            f"({self.published:%Y-%m-%d %H:%M}): "
            f"{self.title}"
            f"{self.content}"
            f"{self.image}"
            f"{self.visibility}"
        )

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

    @staticmethod
    def get_or_404(id):
        try:
            posts = Posts.objects.filter(id=id)
            post = None
            if posts.exists():
                post = posts[0]
            return post
        except:
            return None


class Comment(models.Model):
    class Meta:
        ordering = ["-published"]

    type = "comment"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    published = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("stream-home")


class LikeHistory(models.Model):
    class Meta:
        ordering = ["-add_time"]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)

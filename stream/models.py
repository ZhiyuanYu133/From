from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import AuthUser
import uuid


class Comment(models.Model):
    # In API
    type = "comment"
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE)
    comment = models.TextField()
    contentType = models.TextField(default = "type placeholder")
    published = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    def __str__(self):
        return '%s  : %s' % (self.main_post.title, self.comment)
    
    def get_absolute_url(self):
        return reverse("stream-home")


# Create your models here.
class Post(models.Model):
    # In the API
    type = "post"
    title = models.CharField(max_length=100)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    source = models.CharField(max_length=100, null=True)
    origin = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    contentType = models.CharField(max_length=150, blank=True, null=True)
    content = models.TextField()                               # TextField can have more than 255 characters
    author = models.ForeignKey(AuthUser, on_delete=models.CASCADE, null=True)
    categories = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(default=0, null=True)
    comments = models.ManyToManyField(Comment, blank=True)
    published = models.DateTimeField(default=timezone.now, null=True) 
    image = models.ImageField(upload_to="uploads/post_photo", blank=True, null=True)   
    visibility = models.CharField(max_length=150, blank=True, null=True)
    unlisted = models.BooleanField(default=False, null=True)
    

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
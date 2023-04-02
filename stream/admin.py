from django.contrib import admin
from .models import Posts
@admin.register(Posts)
class UserAdmin(admin.ModelAdmin):
    list_display = ["title", "source", "published"]
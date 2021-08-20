from django.contrib import admin
from .models import Post, Comment, UserProfile, Notification, ThreadModel

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(UserProfile)
admin.site.register(Notification)
admin.site.register(ThreadModel)

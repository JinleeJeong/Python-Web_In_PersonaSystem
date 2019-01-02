from django.contrib import admin

# Register your models here.
from facebook.models import Article
from facebook.models import Comment
admin.site.register(Article)
admin.site.register(Comment)
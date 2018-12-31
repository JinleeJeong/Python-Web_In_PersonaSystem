from django.contrib import admin

# Register your models here.
from facebook.models import Article
from facebook.models import Page, Comment
admin.site.register(Article)
admin.site.register(Page)
admin.site.register(Comment)
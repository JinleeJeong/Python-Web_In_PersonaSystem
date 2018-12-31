"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from facebook.views import newsfeed,detail_feed, new_feed, event, profile, play_two, play, page, remove_feed, edit_feed, fail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('play/', play),
    path('play_two/', play_two),
    path('Daniel/profile/', profile),
    path('event/', event),
    path('newsfeed/', newsfeed),
    path('feed/<pk>/', detail_feed),
    path('page/', page),
    path('new_feed/', new_feed),
    path('feed/<pk>/remove/', remove_feed),
    path('feed/<pk>/edit/', edit_feed),
    path('fail/', fail)
]
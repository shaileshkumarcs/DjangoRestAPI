from django.conf.urls import  url
from django.contrib import admin

from .views import (
        PostListAPIView,
        PostDetailsAPIView
    )


urlpatterns = [
    url(r'^$', PostListAPIView.as_view(), name='list'),
    # url(r'^create/$', post_create),
    url(r'^(?P<slug>[\w-]+)/$', PostDetailsAPIView.as_view(), name='detail'),
    # url(r'^(?P<slug>[\w-]+)/edit/$', post_update, name='update'),
    # url(r'^(?P<slug>[\w-]+)/delete/$', post_delete),
]
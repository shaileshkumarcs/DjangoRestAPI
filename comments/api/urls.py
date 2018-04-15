from django.conf.urls import url
from django.contrib import admin

from .views import(
    CommentCreateAPIView,
    CommentsDetailsAPIView,
    #CommentsEditAPIView,
    CommentsListAPIView,

)


urlpatterns = [
    url(r'^$', CommentsListAPIView.as_view(), name='list'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', CommentsDetailsAPIView.as_view(), name='thread'),
    #url(r'^(?P<pk>\d+)/edit/$', CommentsEditAPIView.as_view(), name='edit'), #delete
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
from django.conf.urls import url
from django.contrib import admin

from .views import(
    CommentsListAPIView,
    CommentsDetailsAPIView,
)


urlpatterns = [
    url(r'^$', CommentsListAPIView.as_view(), name='List'),
    url(r'^(?P<pk>\d+)/$', CommentsDetailsAPIView.as_view(), name='thread'),
    #url(r'^(?P<id>\d+)/delete/$', comment_delete, name='delete'),
]
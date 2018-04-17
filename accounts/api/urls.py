from django.conf.urls import url
from django.contrib import admin

from .views import(
    UserCreateAPIView,
    UserLoginAPIView,
    ListStudent,
    CreateBtechView
)


urlpatterns = [
    url(r'^login', UserLoginAPIView.as_view(), name='login'),
    url(r'^register$', UserCreateAPIView.as_view(), name='list'),
    url(r'^test$', ListStudent.as_view(), name='test'),
    url(r'^create-student$', CreateBtechView.as_view(), name='create'),

]
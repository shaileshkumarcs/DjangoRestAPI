from django.db.models import Q
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.views.generic import TemplateView

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    RetrieveUpdateAPIView
)

from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

from posts.api.permissions import IsOwnerOrReadOnly
from posts.api.pagination import PostLimtOffsetPagination, PostPageNumberPagination

from accounts.models import Btech

from .serializers import (BtechSerializer,BtechSaveSerializer)

User = get_user_model()

from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,
)


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class ListStudent(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Btech.objects.all()
        serializer_class = BtechSerializer(queryset, many=True)

        # permission_classes = [AllowAny]
        return Response(serializer_class.data)

class CreateBtechView(CreateAPIView):
    model = Btech
    permission_classes = (AllowAny,)
    serializer_class = BtechSaveSerializer


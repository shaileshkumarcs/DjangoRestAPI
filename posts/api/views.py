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

from posts.models import Post

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    PostCreateUpdateSerializer,
    PostListSerializer,
    PostDetailsSerializer
    )

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class PostDetailsAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    lookup_field = "slug"
   # lookup_url_kwarg = "abc"

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateUpdateSerializer
    lookup_field = "slug"
   # lookup_url_kwarg = "abc"
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class PostDeleteAPIView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    lookup_field = "slug"
   # lookup_url_kwarg = "abc"

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

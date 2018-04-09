from rest_framework.generics import ListAPIView, RetrieveAPIView

from posts.models import Post
from .serializers import PostListSerializer, PostDetailsSerializer

class PostDetailsAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDetailsSerializer
    lookup_field = "slug"
   # lookup_url_kwarg = "abc"

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer

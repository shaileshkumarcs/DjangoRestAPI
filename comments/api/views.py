from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,
    OrderingFilter
)

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

from comments.models import Comments

from .serializers import (
    CommentsSerializer,
    CommentsDetailSerializer,
    create_comments_serializer,
    )

class CommentCreateAPIView(CreateAPIView):
    queryset = Comments.objects.all()
    #serializer_class = PostCreateUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        medel_type = self.request.GET.get("type")
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comments_serializer(
            model_type='post',
            slug=None,
            parent_id=None,
            user = self.request.user
        )

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

class CommentsDetailsAPIView(RetrieveAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsDetailSerializer
    lookup_field = "pk"
   # lookup_url_kwarg = "abc"

# class PostUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostCreateUpdateSerializer
#     lookup_field = "slug"
#    # lookup_url_kwarg = "abc"
#     permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
#
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)

# class PostDeleteAPIView(DestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostDetailsSerializer
#     lookup_field = "slug"
#    # lookup_url_kwarg = "abc"

class CommentsListAPIView(ListAPIView):
    serializer_class = CommentsSerializer
    filter_backends = [SearchFilter]
    search_fields = ['content','user__first_name']

    pagination_class = PostPageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(PostListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Comments.objects.all() # filter(user= self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return queryset_list
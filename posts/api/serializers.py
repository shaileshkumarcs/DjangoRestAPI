from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            #'id',
            'title',
            #'slug',
            'content',
            'publish',
        ]


class PostDetailsSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'content',
            'publish',
        ]


class PostListSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'user',
            'title',
            'slug',
            'content',
            'publish',
        ]




""""
from posts.models import Post
from posts.api.serializers import PostDetailsSerializer

data = {
    "title": "Yeahh buddy",
    "content": "New Content",
    "publish": "2016-2-12",
    "slug": "Yeahh-Buddy",
}
obj = Post.objects.get(id=2)
new_item = PostDetailsSerializer(obj, data=data)
if new_item.is_valid():
    new_item.save()
else:
    print(new_item.errors)

"""
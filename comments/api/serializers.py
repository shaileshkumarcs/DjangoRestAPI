from rest_framework.serializers import (
    ModelSerializer,
    HyperlinkedIdentityField,
    SerializerMethodField,
)

from comments.models import Comments

class CommentsSerializer(ModelSerializer):
    reply_count = SerializerMethodField()
    class Meta:
        model = Comments
        fields = [
            'id',
            'content_type',
            'object_id',
            'parent',
            'content',
            'reply_count',
            'timestamp'
        ]

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0


class CommentsChildSerializer(ModelSerializer):
    class Meta:
        model = Comments
        fields = [
            'id',
            'content',
            'timestamp'
        ]

class CommentsDetailSerializer(ModelSerializer):
    replies = SerializerMethodField()
    reply_count = SerializerMethodField()
    class Meta:
        model = Comments
        fields = [
            'id',
            'content_type',
            'object_id',
            'content',
            'reply_count',
            'replies',
            'timestamp'
        ]

    def get_replies(self, obj):
        if obj.is_parent:
            return CommentsChildSerializer(obj.children(), many=True).data
        return None

    def get_reply_count(self, obj):
        if obj.is_parent:
            return obj.children().count()
        return 0
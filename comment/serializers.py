from rest_framework import serializers
from comment.models import Comment

from post.serializers import PostSerializer

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
    def to_representation(self, instance):
        self.fields['post'] = PostSerializer(read_only=True)
        return super.to_representation(instance)

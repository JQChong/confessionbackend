from rest_framework import serializers
from post.models import Post

from category.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    num_comments = serializers.SerializerMethodField('get_num_comments')

    def get_num_comments(self, post):
        return post.comments.filter(approved=True).count()

    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['category'] = CategorySerializer(read_only=True, many=True)
        return super().to_representation(instance)

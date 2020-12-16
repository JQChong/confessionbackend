from rest_framework import serializers
from post.models import Post

from category.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['category'] = CategorySerializer(read_only=True, many=True)
        return super().to_representation(instance)

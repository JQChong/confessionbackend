from rest_framework import generics

from post.models import Post
from post.serializers import PostSerializer

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    def get_queryset(self):
        approved = self.request.GET.get('approved', None)
        current_query_set = Post.objects.all()
        if approved is not None:
            current_query_set = current_query_set.filter(approved=approved)
        return current_query_set

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
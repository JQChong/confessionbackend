from rest_framework import generics

from comment.models import Comment
from comment.serializers import CommentSerializer

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        approved = self.request.GET.get('approved', None)
        post_id = self.request.GET.get('post_id', None)
        current_query_set = Comment.objects.all()
        if approved is not None:
            current_query_set = current_query_set.filter(approved=approved)
        if post_id is not None:
            current_query_set = current_query_set.filter(post_id=post_id)
        return current_query_set


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
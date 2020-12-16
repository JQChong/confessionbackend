from rest_framework import generics

from comment.models import Comment
from comment.serializers import CommentSerializer

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    def get_queryset(self):
        approved = self.request.GET.get('approved', None)
        post_id = self.request.GET.get('post_id', None)
        ordering = self.request.GET.getlist('order_by', None)
        current_query_set = Comment.objects.all()
        if approved is not None:
            current_query_set = current_query_set.filter(approved=approved)
        if post_id is not None:
            current_query_set = current_query_set.filter(post_id=post_id)
        if ordering is not None:
            test_obj = current_query_set.first()
            """
            in the event that someone decided to meddle around with the query parameters,
            the list will be sorted by the default way, i.e. by likes and time created
            in descending order.
            """
            def check_all_attr(obj, arr):
                for attr in arr:
                    if getattr(obj, attr, None) is None:
                        return False
                return True
            if check_all_attr(test_obj, ordering):
                current_query_set = current_query_set.order_by(*ordering)
            else:
                current_query_set = current_query_set.order_by('-likes', '-time_created')
        else:
            current_query_set = current_query_set.order_by('-likes', '-time_created')
        return current_query_set


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
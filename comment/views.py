import random

from rest_framework import generics, status

from comment.models import Comment
from comment.serializers import CommentSerializer
from rest_framework.response import Response

from confessionbackend.paginationsettings import PaginationSettings

from rest_framework_simplejwt.authentication import JWTAuthentication

class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    pagination_class = PaginationSettings

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
    
    def create(self, request, *args, **kwargs):
        if self.request.data['approved']:
            return Response({'message': 'Object should not contain approved flag.'}, status=status.HTTP_403_FORBIDDEN)
        return super().create(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        instance = serializer.save()
        data = self.request.data
        if data['poster'] == 'Anonymous':
            number = str(random.randint(1000, 9999))
            anonId = number[:2] + str(instance.id) + number[2:]
            serializer.save(poster='Anonymous#' + anonId)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def update(self, request, *args, **kwargs):
        if self.request.method == 'PUT':
            return Response({'message': "METHOD NOT ALLOWED"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
        if self.request.method == 'PATCH':
            if self.request.data['approved'] and not JWTAuthentication().authenticate(self.request):
                return Response({'message': 'ILLEGAL OPERATION'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        if not JWTAuthentication().authenticate(self.request):
            return Response({'message': 'ILLEGAL OPERATION'}, status=status.HTTP_401_UNAUTHORIZED)
        return super().destroy(request, *args, **kwargs)
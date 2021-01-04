from rest_framework import generics

from post.models import Post
from post.serializers import PostSerializer
from rest_framework.response import Response

from confessionbackend.paginationsettings import PaginationSettings

class PostList(generics.ListCreateAPIView):
    serializer_class = PostSerializer
    pagination_class = PaginationSettings

    def get_queryset(self):
        approved = self.request.GET.get('approved', None)
        category = self.request.GET.get('category', None)
        search = self.request.GET.get('search', None)
        current_queryset = Post.objects.all().order_by('-time_created', '-likes')
        if approved is not None:
            current_queryset = current_queryset.filter(approved=approved)
        if category is not None:
            current_queryset = current_queryset.filter(category__in=[category])
        if search is not None:
            current_queryset = current_queryset.filter(text__icontains=search)
        return current_queryset

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        post_id = kwargs['pk']
        current_queryset = self.get_queryset().filter(approved=True)
        prev_instance = current_queryset.filter(id__lt=post_id).order_by('-id').first()
        next_instance = current_queryset.filter(id__gt=post_id).order_by('id').first()

        prev_id = prev_instance.id if prev_instance else -1
        next_id = next_instance.id if next_instance else -1
        return Response({"data": serializer.data, "prev_id": prev_id, "next_id": next_id})
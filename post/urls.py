from django.urls import path

from post.views import PostList, PostDetail

urlpatterns = [
    path('posts', PostList.as_view()),
    path('posts/<int:pk>', PostDetail.as_view())
]
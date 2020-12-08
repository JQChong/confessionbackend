from django.urls import path

from comment.views import CommentList, CommentDetail, CommentByPost

urlpatterns = [
    path('comments', CommentList.as_view()),
    path('comments/<int:pk>', CommentDetail.as_view()),
    path('comments/post/<int:post_id>', CommentByPost.as_view())
]
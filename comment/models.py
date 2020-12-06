from django.db import models
from post.models import Post

class Comment(models.Model):
    """
    comment id is again the surrogate key so will not be included here
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    text = models.TextField(blank=False, null=False, default='')
    likes = models.PositiveIntegerField(default=0)
    time_created = models.DateTimeField(auto_now=True)
    poster = models.CharField(max_length=256, blank=False, null=False, default='Anonymous')

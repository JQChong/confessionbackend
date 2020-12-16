from django.db import models

# Create your models here.
class Category(models.Model):
    """
    this class is needed as django doesn't exactly support multi-valued
    attribute.
    """
    name = models.CharField(max_length=256, blank=False, null=False, default="No Category")

    def __str__(self):
        return self.name

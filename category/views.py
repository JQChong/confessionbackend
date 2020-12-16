from rest_framework import generics

from category.models import Category
from category.serializers import CategorySerializer

# Create your views here.
class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

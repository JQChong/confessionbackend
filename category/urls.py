from django.urls import path

from category.views import CategoryList

urlpatterns = [
    path('category', CategoryList.as_view())
]
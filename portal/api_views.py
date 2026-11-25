from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Employee, Tag, WallPost
from .serializers import EmployeeSerializer, TagSerializer, WallPostSerializer


class WallPostListAPI(generics.ListAPIView):
    serializer_class = WallPostSerializer

    def get_queryset(self):
        qs = WallPost.objects.select_related("tag").order_by("-created_at")
        tag_name = self.request.query_params.get("tag")
        if tag_name:
            qs = qs.filter(tag__name=tag_name)
        return qs

class TagListAPI(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class EmployeePagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = "page_size"
    max_page_size = 100


class EmployeeListAPI(generics.ListAPIView):
    serializer_class = EmployeeSerializer
    pagination_class = EmployeePagination

    def get_queryset(self):
        return Employee.objects.select_related("team", "manager").order_by("name")
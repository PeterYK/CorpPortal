from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Employee, InfoArticle, Tag, Team, WallPost
from .serializers import (
    EmployeeSerializer,
    InfoArticleSerializer,
    TagSerializer,
    TeamDetailSerializer,
    TeamSerializer,
    WallPostSerializer,
)


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

class TeamListAPI(generics.ListAPIView):
    queryset = Team.objects.all().order_by("name")
    serializer_class = TeamSerializer

class InfoArticleListAPI(generics.ListAPIView):
    queryset = InfoArticle.objects.all().order_by("title")
    serializer_class = InfoArticleSerializer

class WallPostDetailAPI(generics.RetrieveAPIView):
    queryset = WallPost.objects.select_related("tag")
    serializer_class = WallPostSerializer

class EmployeeDetailAPI(generics.RetrieveAPIView):
    queryset = Employee.objects.select_related("team", "manager")
    serializer_class = EmployeeSerializer

class TeamDetailAPI(generics.RetrieveAPIView):
    queryset = Team.objects.prefetch_related("leaders", "members")
    serializer_class = TeamDetailSerializer

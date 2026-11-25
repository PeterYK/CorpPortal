from rest_framework import generics

from .models import Tag, WallPost
from .serializers import TagSerializer, WallPostSerializer


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

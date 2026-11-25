# from django.shortcuts import render
from django.views.generic import ListView

from .models import Tag, WallPost


class WallListView(ListView):
    model = WallPost
    template_name = "wall.html"
    context_object_name = "posts"
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset().select_related("tag")
        tag_name = self.request.GET.get("tag")
        if tag_name:
            qs = qs.filter(tag__name=tag_name)
        return qs.order_by("-created_at")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tags"] = Tag.objects.all()
        context["current_tag"] = self.request.GET.get("tag")
        return context

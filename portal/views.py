# from django.shortcuts import render
from django.http import JsonResponse
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

def wall_posts_api(request):
    tag_name = request.GET.get("tag")
    qs = WallPost.objects.select_related("tag").order_by("-created_at")
    if tag_name:
        qs = qs.filter(tag__name=tag_name)

    data = [
        {
            "id": p.id,
            "title": p.title,
            "content": p.content,
            "company": p.company,
            "created_at": p.created_at.isoformat(),
            "tag": p.tag.name,
        }
        for p in qs
    ]
    return JsonResponse({"posts": data})


def wall_tags_api(request):
    tags = list(Tag.objects.values_list("name", flat=True))
    return JsonResponse({"tags": tags})
# from django.shortcuts import render
from django.db.models import Q
from django.views.generic import DetailView, ListView

from .models import Employee, InfoArticle, Tag, Team, WallPost


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

class ColleaguesListView(ListView):
    model = Employee
    template_name = "colleagues.html"
    context_object_name = "employees"
    paginate_by = 20

    def get_queryset(self):
        qs = Employee.objects.select_related("team", "manager").order_by("name")
        q = self.request.GET.get("q", "").strip()
        if q:
            qs = qs.filter(
                Q(name__icontains=q) |
                Q(position__icontains=q) |
                Q(city__icontains=q) |
                Q(team__name__icontains=q) |
                Q(email__icontains=q) |
                Q(telegram__icontains=q)
            )
        return qs

class TeamsListView(ListView):
    model = Team
    template_name = "teams.html"
    context_object_name = "teams"

    def get_queryset(self):
        return Team.objects.all().order_by("name")

class UsefulInfoListView(ListView):
    model = InfoArticle
    template_name = "useful_info.html"
    context_object_name = "articles"

    def get_queryset(self):
        return InfoArticle.objects.all().order_by("title")

class WallPostDetailView(DetailView):
    model = WallPost
    template_name = "wall_post_detail.html"
    context_object_name = "post"


# ruff: noqa: RUF012
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import (
    Employee,
    InfoArticle,
    Project,
    Team,
    TimeAllocation,
    UserProfile,
    WallPost,
)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "Профиль"
    fk_name = "user"

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
    
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'team', 'city', 'email']
    list_filter = ['team', 'city']
    search_fields = ['name', 'email', 'position']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    filter_horizontal = ['leaders']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(WallPost)
class WallPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'tag', 'company', 'created_at']
    list_filter = ['tag']

@admin.register(InfoArticle)
class InfoArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    filter_horizontal = ['contacts']

@admin.register(TimeAllocation)
class TimeAllocationAdmin(admin.ModelAdmin):
    list_display = ['employee', 'project', 'date', 'hours']
    list_filter = ['date', 'project']


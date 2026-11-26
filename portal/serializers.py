# ruff: noqa: RUF012

from rest_framework import serializers

from .models import Employee, InfoArticle, Tag, Team, WallPost


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class WallPostSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(source="tag.name", read_only=True)

    class Meta:
        model = WallPost
        fields = ["id", "title", "content", "company", "created_at", "tag"]

class TeamShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name"]
  
             
class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ["id", "name", "description", "mascot_icon"]

class EmployeeSerializer(serializers.ModelSerializer):
    team = TeamSerializer(read_only=True, allow_null=True)
    manager_id = serializers.IntegerField(source="manager.id", read_only=True, allow_null=True)
    manager_name = serializers.CharField(source="manager.name", read_only=True, allow_null=True)

    class Meta:
        model = Employee
        fields = [
            "id", "name", "position", "city", "birthday",
            "email", "telegram", "team", "manager_id", "manager_name"
        ]

class InfoArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoArticle
        fields = ["id", "title", "content"]

class TeamDetailSerializer(serializers.ModelSerializer):
    leaders = EmployeeSerializer(many=True, read_only=True)
    members = EmployeeSerializer(many=True, read_only=True)

    class Meta:
        model = Team
        fields = ["id", "name", "description", "mascot_icon", "leaders", "members"]

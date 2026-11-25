# ruff: noqa: RUF012

from rest_framework import serializers

from .models import Employee, Tag, Team, WallPost


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


class EmployeeSerializer(serializers.ModelSerializer):
    team = TeamShortSerializer(read_only=True)
    manager_name = serializers.CharField(source="manager.name", read_only=True, allow_null=True)

    class Meta:
        model = Employee
        fields = ["id", "name", "position", "team", "manager_name", "city", "email", "telegram", "birthday"]
        

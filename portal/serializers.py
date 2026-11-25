# ruff: noqa: RUF012

from rest_framework import serializers

from .models import Tag, WallPost


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ["id", "name"]

class WallPostSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(source="tag.name", read_only=True)

    class Meta:
        model = WallPost
        fields = ["id", "title", "content", "company", "created_at", "tag"]

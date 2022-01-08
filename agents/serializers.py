from rest_framework import serializers
from .models import Agent, Chart


class AgentsSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "author", "department", "published")
        model = Agent


class TeamLeadersSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "")

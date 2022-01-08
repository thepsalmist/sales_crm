from rest_framework import serializers
from .models import Agent, TeamLead


class TeamLeadersSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="user-detail",
        lookup_field="email",
    )

    department = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="department-detail",
    )

    class Meta:
        fields = ("id", "user", "region", "department", "phone_number")
        model = TeamLead


class AgentsSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="user-detail",
        lookup_field="email",
    )

    department = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="department-detail",
    )
    supervisor = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name="supervisor-detail",
    )

    class Meta:
        fields = ("id", "user", "supervisor", "department", "phone_number")
        model = Agent

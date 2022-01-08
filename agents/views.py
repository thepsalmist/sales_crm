from django.shortcuts import render
from rest_framework import generics
from .models import Agent, TeamLead
from .serializers import TeamLeadersSerializer, AgentsSerializer
from rest_framework.permissions import IsAdminUser


class AgentsListView(generics.ListAPIView):
    """
    View the list of all agents
    """

    queryset = Agent.objects.all()
    serializer_class = AgentsSerializer


class AgentsCreateView(generics.ListCreateAPIView):
    """
    View the list of all agents
    """

    queryset = Agent.objects.all()
    serializer_class = AgentsSerializer


class TeamLeadersListView(generics.ListAPIView):
    """
    View the list of all team leaders
    """

    queryset = TeamLead.objects.all()
    serializer_class = TeamLeadersSerializer


class AgentsDetail(generics.RetrieveDestroyAPIView):
    queryset = Agent.objects.all()
    serializer_class = AgentsSerializer


class TeamLeadersDetail(generics.RetrieveDestroyAPIView):
    queryset = TeamLead.objects.all()
    serializer_class = TeamLeadersSerializer

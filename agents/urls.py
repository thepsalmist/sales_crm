from django.urls import path
from .views import TeamLeadersListView, TeamLeadersDetail, AgentsListView, AgentsDetail

app_name = "agents"

urlpatterns = [
    path("agents_list/", AgentsListView.as_view(), name="agents"),
    path("team_leders_list/", AgentsListView.as_view(), name="agents"),
]

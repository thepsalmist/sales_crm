from django.urls import path
from .views import 

app_name = "agents"

urlpatterns = [
    path("", ChartsListView.as_view(), name="charts"),
]
from django.db import models

from authentication.models import CustomUser


class TeamLead(models.Model):
    """
    Team leaders model
    """

    REGION_CHOICES = (
        ("nairobi", "Nairobi"),
        ("mombasa", "Mombasa"),
        ("kisumu", "Kisumu"),
    )
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="team_leaders"
    )
    region = models.CharField(choices=REGION_CHOICES, max_length=256)
    phone_number = models.CharField(max_length=256)


class Agent(models.Model):
    """
    Agents model
    """

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="agents"
    )
    supervisor = models.ForeignKey(TeamLead, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256)

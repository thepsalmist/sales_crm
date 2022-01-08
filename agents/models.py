from django.db import models

from authentication.models import CustomUser


class Department(models.Model):
    """
    Model to represent Departments - Organizations Department
    """

    DEPARTMENTS = (
        ("sales", "Sales"),
        ("finance", "Finance"),
        ("engineering", "Engineering"),
    )
    name = models.CharField(choices=DEPARTMENTS, max_length=20)

    def __str__(self) -> str:
        return self.name


class TeamLead(models.Model):
    """
    Model to represent team leaders
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
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.user.email} region {self.region}"


class Agent(models.Model):
    """
    Model to represent Agents
    """

    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, related_name="agents"
    )
    supervisor = models.ForeignKey(TeamLead, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=256)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

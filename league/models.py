from django.db import models
from django.db.models import JSONField

from club.models import Team


class League(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Group(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return 'Group_' + str(self.id)

class GroupTeam(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    num_matches_played = models.IntegerField(default=0)
    num_wins = models.IntegerField(default=0)
    num_draws = models.IntegerField(default=0)
    num_losses = models.IntegerField(default=0)
    goals_scored = models.IntegerField(default=0)
    goals_conceded = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    match_outcomes = JSONField(default=list)

    class Meta:
        unique_together = ('group', 'team')
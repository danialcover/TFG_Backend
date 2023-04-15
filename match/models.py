from django.db import models

from club.models import Team, Location
from league.models import Group
from user.models import Profile


class Match(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True)
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='team2')
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    date = models.DateTimeField(null=True, blank=True) #YYYY-MM-DDThh:mm:ss
    team1_result = models.IntegerField(null=True, blank=True)
    team2_result = models.IntegerField(null=True, blank=True)
    comments = models.CharField(max_length=200, null=True, blank=True)
    def __str__(self):
        return 'Match_' + str(self.id)

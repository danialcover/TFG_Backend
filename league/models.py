from django.db import models

from club.models import Team


class League(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Group(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    teams = models.ManyToManyField(Team)

    def __str__(self):
        return 'Group_' + str(self.id)

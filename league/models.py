from django.db import models


class League(models.Model):
    name = models.CharField(max_length=30)
    year = models.IntegerField()

    def __str__(self):
        return self.name


class Group(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)

    def __str__(self):
        return 'group_' + str(self.id)

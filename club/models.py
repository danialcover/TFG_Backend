from django.db import models


class Club(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=30)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Location(models.Model):
    address = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

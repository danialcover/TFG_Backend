from django.db import models

class User(models.Model):
    name = models.CharField(max_length=30)

class League(models.Model):
    name = models.CharField(max_length=30)
    any = models.IntegerField()

class Group(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)

class Club(models.Model):
    name = models.CharField(max_length=30)

class Team(models.Model):
    name = models.CharField(max_length=30)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

class Location(models.Model):
    address = models.CharField(max_length=40)
    postal_code = models.CharField(max_length=5)
    city = models.CharField(max_length=30)
    club = models.ForeignKey(Club, on_delete=models.CASCADE)

class Match(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

class Rol(models.Model):
    name = models.CharField(max_length=30)

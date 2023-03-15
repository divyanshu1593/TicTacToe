from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

def df():
    return [2,2,2]

class GameData(models.Model):
    grid = ArrayField(ArrayField(models.IntegerField(default=2),default=df,size=3),default=df,size=3)
    isLogin = models.BooleanField(default=False)
    gameWon = models.IntegerField(default=0)
    gameDrawn = models.IntegerField(default=0)
    gameLost = models.IntegerField(default=0)
    numberOfGames = models.IntegerField(default=0)

class UserInfo(models.Model):
    username = models.CharField(max_length=100, default="")
    password = models.CharField(max_length=100, default="")
    name = models.CharField(max_length=100, default="")
    gameWon = models.IntegerField(default=0)
    gameDrawn = models.IntegerField(default=0)
    gameLost = models.IntegerField(default=0)
    numberOfGames = models.IntegerField(default=0)

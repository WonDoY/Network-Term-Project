from django.db import models

# Create your models here.

# player 정보 class명 PlayerInfo
class PlayerInfo(models.Model):
    Playername = models.CharField(max_length = 15)

    def __str__(self):
        return self.Playername
    

class Room(models.Model):
    Playername = models.CharField(max_length = 15)
    Room_full = models.IntegerField(default=0)
    Player1 = models.CharField(max_length=15,default = 'Unknown')
    Player2 = models.CharField(max_length=15,default = 'Unknown')

    

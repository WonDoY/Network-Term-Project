from django.db import models

# Create your models here.

# player 정보 class명 PlayerInfo
class PlayerInfo(models.Model):
    Playername = models.CharField(max_length = 15)

    def __str__(self):
        return self.Playername
    
# 방 정보 class명 Room
class Room(models.Model):
    Playername = models.CharField(max_length = 15)
    Room_full = models.IntegerField(default=0)
    Player1 = models.CharField(max_length=15,default = 'Unknown')
    Player2 = models.CharField(max_length=15,default = 'Unknown')
# Player1,2 , 방 가득찬 경우 Room_full

# 게임판 정보 board, num는 방 번호    
class Board(models.Model):
    board = models.TextField()
    num = models.IntegerField(default=0)

    

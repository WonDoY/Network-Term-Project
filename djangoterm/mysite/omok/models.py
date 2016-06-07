from django.db import models

# Create your models here.

# 게임판 정보 board, num는 방 번호    
class omokBoard(models.Model):
    board = models.TextField()
    room_num = models.IntegerField(default=0)

# player 정보 class명 PlayerInfo
class UserInfo(models.Model):
    name = models.CharField(max_length = 15)
       
    count = 0

    def __str__(self):
        return self.name
    
# 방 정보 class명 Room
class RoomInfo(models.Model):
    name = models.CharField(max_length = 15)
    pull = models.IntegerField(default=0)
    user1 = models.CharField(max_length=15,default = 'none')
    user2 = models.CharField(max_length=15,default = 'none')
# Player1,2 , 방 가득찬 경우 Room_full    

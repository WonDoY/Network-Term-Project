from django.contrib import admin
from .models import PlayerInfo
from .models import Room
from .models import Board
# Register your models here.

# Omok Object

admin.site.register(PlayerInfo)
admin.site.register(Room)
admin.site.register(Board)

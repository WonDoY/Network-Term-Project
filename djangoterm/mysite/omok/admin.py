from django.contrib import admin
from .models import omokBoard, UserInfo, RoomInfo

# Register your models here.

# Omok Object


admin.site.register(omokBoard)
admin.site.register(UserInfo)
admin.site.register(RoomInfo)

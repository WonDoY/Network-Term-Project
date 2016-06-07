from django.contrib import admin
from .models import UserInfo , RoomInfo, omokBoard

# Register your models here.

# Omok Object


admin.site.register(UserInfo)
admin.site.register(RoomInfo)
admin.site.register(omokBoard)

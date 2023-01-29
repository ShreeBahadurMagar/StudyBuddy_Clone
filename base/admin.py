from django.contrib import admin

# Register your models here.
from.models import Room, Topic,Message,User
# registering the database in DB as named room
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)

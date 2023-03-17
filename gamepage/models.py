from django.db import models

from datetime import datetime
# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=1000)

class Message(models.Model):
    value= models.CharField(max_length=50000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=1000)
    room = models.CharField(max_length=1000)
class ConnectedUser(models.Model):
    user = models.CharField(max_length=1000)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    connected_at = models.DateTimeField(auto_now_add=True)

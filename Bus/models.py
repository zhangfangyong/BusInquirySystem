from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=20,primary_key=True)
    password = models.CharField(max_length=20)

class Station(models.Model):
    stationname = models.CharField(max_length=20,primary_key=True)
    building = models.CharField(max_length=40)

class SiteRoute(models.Model):
    stationname = models.ForeignKey("Station",on_delete=models.CASCADE)
    busid = models.CharField(max_length=20)
    siteinbus = models.IntegerField()

class Route(models.Model):
    busid = models.CharField(max_length=20,primary_key=True)
    route = models.CharField(max_length=200)

class News(models.Model):
    title = models.CharField(max_length=100,primary_key=True)
    content = models.TextField()
    time = models.DateField()
    def __str__(self):
        return self.title
    def toDict(self):
        return {u'title': self.title, u'content': self.content, u'time': self.time.strftime('%Y-%m-%d')}




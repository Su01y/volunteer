import geocoder 

from django.db import models

# Create your models here.

mapbox_access_token = 'pk.eyJ1IjoiZXJtYWsyMjgiLCJhIjoiY2wzbGt4aDk3MDIzcDNqcGhiNzM1Z212OSJ9.GhHG9-_9zTge3GnRuEitCA'

class Task(models.Model):
    taskname = models.CharField(max_length=200, default='')
    organization = models.CharField(max_length=200, default='')
    address = models.TextField()
    description = models.TextField()
    required_quantity = models.IntegerField()
    available_quantity = models.IntegerField()
    lat = models.FloatField(blank=True, null=True)
    long = models.FloatField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        g = geocoder.mapbox(self.address, key=mapbox_access_token)
        g = g.latlng
        self.lat = g[0]
        self.long = g[1]
        return super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.taskname

    class Meta:
        db_table = 'task'
from django.db import models

# Create your models here.
class Volunteer(models.Model):
    username = models.CharField(max_length=40)
    password = models.CharField(max_length=40)
    email = models.EmailField(default='')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'volunteer'

# class Task(models.Model):
#     taskname = models.CharField()
#     position = models.
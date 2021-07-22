from django.db import models
import datetime

# Create your models here.
class Rate(models.Model):
    ident = models.CharField(max_length=3)
    rate = models.IntegerField()
    time_point = models.DateTimeField(db_index=True)

class User(models.Model):
    mail = models.EmailField()
    key = models.CharField(max_length=50, db_index=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    role = models.IntegerField() #0 - denied_all, 1 - r, 2 - rw
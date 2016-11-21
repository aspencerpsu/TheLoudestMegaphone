from __future__ import unicode_literals

from django.db import models
import uuid

class GunVioleceArchive(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=120, default=None, blank=True, null=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=10)
    is_police_involved = models.BooleanField(default=False)

    def __unicode__ (self):
        return self.id

class Incident(models.Model):
	uid=models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
	date = models.DateField(auto_now=False, auto_now_add=False)
	address = models.CharField(max_length=120, default=None, blank=True, null=True)
	city = models.CharField(max_length=120)
	state = models.CharField(max_length=2)
	source = models.CharField(max_length=4096)
	
	
class Victim(models.Model):
    incident=models.ForeignKey(Incident,on_delete=models.CASCADE)	
    suicide=models.BooleanField(default=False)
    shot_dead_by_police = models.BooleanField(default=False)
    civilian_injury = models.BooleanField(default=False)
    civilian_death = models.BooleanField(default=False)
    police_injury = models.BooleanField(default=False)
    police_death = models.BooleanField(default=False)
    is_police = models.BooleanField(default=False)

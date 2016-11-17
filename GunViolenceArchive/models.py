from __future__ import unicode_literals

from django.db import models

class GunVioleceArchive(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=120, default=None, blank=True, null=True)
    city = models.CharField(max_length=120)
    state = models.CharField(max_length=10)
    is_police_involved = models.BooleanField(default=False)
    shot_dead_by_police = models.BooleanField(default=False)
    civilian_injury = models.SmallIntegerField(default=0)
    civilian_death = models.SmallIntegerField(default=0)
    police_injury = models.SmallIntegerField(default=0)
    police_death = models.SmallIntegerField(default=0)

    def __unicode__ (self):
        return self.id


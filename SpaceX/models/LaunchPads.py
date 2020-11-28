from django.db import models

class LaunchPads(models.Model):
    id = models.UUIDField()
    name = models.CharField()
    status = models.CharField()
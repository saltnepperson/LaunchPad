import json

from django.db import models

class LaunchPads(models.Model):
    # id must be a string
    id = models.CharField(max_length=24, primary_key=True)
    name = models.CharField(max_length=256)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def all(self):
        data = LaunchPads.objects.all().values('id','name','status')
        data = json.dumps(list(data))
        return data
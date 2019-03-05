from django.db import models
from django.utils.timezone import now


class PPMData(models.Model):
    value = models.IntegerField(default=0)
    date = models.DateTimeField(default=now)

class NowPPM(models.Model):
    value = models.IntegerField(default=0)



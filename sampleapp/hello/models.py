from django.db import models


class Request(models.Model):

    timestamp = models.DateTimeField()


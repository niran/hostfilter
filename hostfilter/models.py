from django.db import models


class Host(models.Model):
    hostname = models.CharField(max_length=255)
    allowed_pattern = models.TextField()

from django.db import models

class tasks(models.Model):
    taskname=models.CharField(max_length=50)
    completed=models.BooleanField(default=False)
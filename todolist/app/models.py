from django.db import models


# Create your models here.

class TodoModel(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField(max_length=1000, blank=False, null=False)
    date = models.DateTimeField()

    def __str__(self):
        return self.title


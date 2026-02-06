from django.db import models

from django.urls import reverse
# Create your models here.

class Task(models.Model):
    content = models.CharField(max_length=100, null=False, blank=True)
    boolen = models.BooleanField(default=False)
    


    def __str__(self):
        return self.title
    

# Create your models here.

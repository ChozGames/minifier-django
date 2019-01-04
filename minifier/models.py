from django.db import models
from django.utils import timezone

class Url(models.Model):
    url = models.CharField(max_length=255)
    code = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)
    pseudo = models.CharField(max_length=30)
    access = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['date']
        
    def __str__(self):
        return self.url

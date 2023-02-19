from django.db import models
from django.urls import reverse

class Entry(models.Model):
    name = models.CharField(max_length=50)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
      return self.name
    

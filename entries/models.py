from django.db import models
from django.urls import reverse

class Entry(models.Model):

    GRADES = [
    ('9', '9'),
    ('10', '10'),
    ('11', '11'),
    ('12', '12'),
    ]


    name = models.CharField(max_length=50, null=True)
    school = models.CharField(max_length=50, null=True)
    grade = models.CharField(max_length=2, choices=GRADES, null=True) 
    email = models.EmailField(max_length=100, null=True)
    file = models.FileField(upload_to='uploads/', null=True)

    def get_absolute_url(self):
        return reverse('index')

    def __str__(self):
      return self.name
    

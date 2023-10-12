"""
Definition of models.
"""

from django.db import models

# Create your models here.

class Pupil(models.Model):
    fio = models.CharField(max_length = 100)
    city = models.CharField(max_length = 30)
    school = models.IntegerField(null = True)
    cls = models.IntegerField(null = True)
    tel = models.CharField(max_length = 20, null = True, blank = True)
    email = models.EmailField(null = True, blank = True)
    info = models.TextField(null = True, blank = True)
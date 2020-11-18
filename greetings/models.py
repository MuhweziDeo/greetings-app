from django.db import models

# Create your models here.

class Greeting(models.Model):
    body = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=True,blank=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,blank=True,editable=False) 
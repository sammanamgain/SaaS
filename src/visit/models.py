from django.db import models

# Create your models here.
class Visit(models.Model):
    
    timeStamp=models.DateTimeField(auto_now=True)
    
from django.db import models
from django.contrib.auth.models import User # Django by default have models; this is for Users; handle authentication

# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True) # CASCASE - to delete the user specific data; SET_NULL - to set the data to null 
    title = models.CharField(max_length=200) # CharField for headline
    description = models.TextField(null=True, blank=True) # TextField for paragraphs
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True) # Automatically add the datetime with the time of adding row

    def __str__(self):
        return self.title

    class Meta: # Setting the metadata of the main class to order by default when getting multiple rows
        ordering = ['complete']
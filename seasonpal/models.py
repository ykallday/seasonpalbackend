from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    location = models.CharField(blank=True, max_length=120)
    def __str__(self):
        return self.username
    

class Produce(models.Model):
    name = models.CharField(blank=True,max_length=100, unique=True)
    category = models.CharField(blank=True,max_length=100)
    image_url = models.TextField()
    description = models.TextField()
    link1 = models.TextField(blank=True)
    link2 = models.TextField(blank=True)
    link3 = models.TextField(blank=True)
    def __str__(self):
        return self.name

class SeasonLocation(models.Model):
    location = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    combo = models.CharField(max_length=100, unique=True)
    produce = models.ManyToManyField(Produce)
    def __str__(self):
        return (self.combo)
    
class Note(models.Model):
    user = models.CharField(max_length=100)
    produce = models.CharField(max_length=100)
    content = models.TextField()
    def __str__(self):
        return self.content

class Suggestion(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField()
    category = models.TextField()
    def __str__(self):
        return self.category


class Resource(models.Model):
    title = models.TextField()
    category = models.CharField(blank=True,max_length=100)
    small_img = models.TextField()
    main_img = models.TextField(blank=True)
    content= models.TextField()
    opt_link = models.TextField(blank=True)
    def __str__(self):
        return self.title
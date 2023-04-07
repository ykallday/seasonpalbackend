from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    location = models.CharField(blank=True, max_length=120)

class SeasonLocation(models.Model):
    location = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
   
    def __str__(self):
        return self.location, self.season
    

class Produce(models.Model):
    name = models.CharField(blank=True,max_length=100)
    category = models.CharField(blank=True,max_length=100)
    image_url = models.TextField()
    description = models.TextField()
    seasonlocations = models.ManyToManyField(SeasonLocation)
    def __str__(self):
        return self.name
    
class Note(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='author', default = 0)
    produce = models.ForeignKey(Produce, on_delete=models.CASCADE, related_name='subject', default = 0)
    content = models.TextField()
    def __str__(self):
        return self.produce

class Suggestion(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='by', default = 0)
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
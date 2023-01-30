from django.db import models
from django.contrib.auth.models import User
from .choice import * 

class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    bigimage=models.URLField()
    image=models.URLField()
    ytlink=models.URLField()
    reserve=models.URLField()
    tomorrow=models.URLField()
    title=models.CharField(max_length=200)
    released=models.DateField(null=True, blank=True)
    genre=models.CharField(max_length=200)
    casts=models.CharField(max_length=200)
    duration=models.CharField(max_length=200)
    country=models.CharField(max_length=200)
    production=models.CharField(max_length=200)
    text=models.TextField()
    regisor=models.CharField(max_length=200)
    

    def __str__(self):
        return f"{self.title}"

class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=25)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    def __str__(self):
        return f"{self.email}"


class Reservation(models.Model):
    name= models.CharField(max_length=255)
    email = models.EmailField()
    phone= models.CharField(max_length=255)
    no_persons=models.PositiveIntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}"

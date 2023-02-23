from django.db import models

# Create your models here.

class Director(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(null=True, blank=True)
    duration=models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE, null=True)


class Review(models.Model):
    text=models.TextField()
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE, null=True)
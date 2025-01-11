from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=100, default='Unknow')
    director = models.CharField(max_length=150, default='Unknow author')
    year = models.IntegerField()
    synopsis = models.TextField()

    def __str__(self):
        return self.title
    



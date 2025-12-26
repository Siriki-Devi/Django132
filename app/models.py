from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    first_movie = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    movies = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name

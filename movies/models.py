from django.db import models
import uuid

class Genre(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.title
    
class Movie(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    director = models.CharField(max_length=200, null=True, blank=True)
    actors = models.CharField(max_length=200, null=True, blank=True)
    created = models.DateField()
    genre = models.ManyToManyField(Genre, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
    
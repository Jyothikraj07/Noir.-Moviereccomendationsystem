from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    release_year = models.IntegerField()
    description = models.TextField()
    avg_rating = models.FloatField(default=0)
    poster = models.URLField(blank=True, null=True)
    tmdb_id = models.IntegerField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title
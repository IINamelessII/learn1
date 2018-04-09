from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Director(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=64)
    duration = models.PositiveIntegerField()
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    genres = models.ManyToManyField(Genre, related_name='movies_genres')
    preview = models.ImageField(upload_to='previews/')
    description = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile_user')
    watched = models.ManyToManyField(Movie, null=True, blank=True, related_name='users_watched')
    watching = models.ManyToManyField(Movie, null=True, blank=True, related_name='users_watching')
    plan_to_watch = models.ManyToManyField(Movie, null=True, blank=True, related_name='users_plan_to_watch')
    favorite = models.ManyToManyField(Movie, null=True, blank=True, related_name='users_favorite')

    def __str__(self):
        return self.user.username


class Rate(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    value = models.IntegerField()

    def __str__(self):
        return f'{self.value} to {self.movie} by {self.user}'

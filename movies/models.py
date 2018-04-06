from django.db import models


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


class User(models.Model):
    login = models.CharField(max_length=16)
    password = models.CharField(max_length=16)
    watched = models.ManyToManyField(Movie, related_name='users_watched')
    watching = models.ManyToManyField(Movie, related_name='users_watching')
    plan_to_watch = models.ManyToManyField(Movie, related_name='users_plan_to_watch')

    def __str__(self):
        return self.login


class Rate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    movie = models.OneToOneField(Movie, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()

    def __str__(self):
        return f'{self.value} to {self.movie} by {self.user}'

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Director, Genre, Movie, User, Rate

def login(request):
    pass


def index(request):
    context = {
        'movies': Movie.objects.all,
        'user': request.user
    }
    return render(request, 'movies/index.html', context)


def movie(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404('Movie does not exist.')
    context = {
        'movie': movie,
        'user': request.user
    }
    return render(request, 'movies/movie.html', context)

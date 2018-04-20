from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .models import Director, Genre, Movie, Profile, Rate

def login(request):
    pass


def index(request):
    context = {
        'movies': Movie.objects.all,
        'user': request.user
    }
    return render(request, 'movies/index.html', context)


def genres(request):
    context = {
        'genres': Genre.objects.all,
        'user': request.user
    }
    return render(request, 'movies/genres.html', context)


def directors(request):
    context = {
        'directors': Director.objects.all,
        'user': request.user
    }
    return render(request, 'movies/directors.html', context)


def profile(request, username):
    try:
        profile = Profile.objects.get(user__username=username)
    except Profile.DoesNotExist:
        raise Http404('Profile does not exist.')
    context = {
        'profile': profile,
        'user': request.user
    }
    return render(request, 'movies/profile.html', context)


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


def genre(request, genre_id):
    try:
        genre = Genre.objects.get(pk=genre_id)
    except Genre.DoesNotExist:
        raise Http404('Genre does not exist.')
    context = {
        'genre': genre,
        'movies_with_genre': Movie.objects.filter(genres__id=genre_id),
        'user': request.user
    }
    return render(request, 'movies/genre.html', context)


def director(request, director_id):
    try:
        director = Director.objects.get(pk=director_id)
    except Director.DoesNotExist:
        raise Http404('Director does not exist.')
    context = {
        'director': director,
        'movies_with_director': Movie.objects.filter(director__id=director_id),
        'user': request.user
    }
    return render(request, 'movies/director.html', context)

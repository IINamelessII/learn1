from django.contrib import admin

from .models import Genre, Movie, Profile, Director, Rate

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(Profile)
admin.site.register(Director)
admin.site.register(Rate)

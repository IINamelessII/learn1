from django.contrib import admin

from .models import Genre, Movie, User, Director, Rate

admin.site.register(Genre)
admin.site.register(Movie)
admin.site.register(User)
admin.site.register(Director)
admin.site.register(Rate)

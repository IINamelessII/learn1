from django.urls import path

from . import views


urlpatterns = [
    path('', views.index),
    path('<int:movie_id>', views.movie)
]

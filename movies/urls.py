import sys
sys.path.append('..')

from django.urls import path

from . import views
from users import views as v



urlpatterns = [
    path('', views.index, name='movies'),
    path('<int:movie_id>', views.movie),
    path('genres/<int:genre_id>', views.genre),
    path('genres', views.genres, name='genres'),
    path('profiles/<str:username>', views.profile, name='profile'),
    path('', v.index, name='index'),
    path('login', v.login_view, name='login'),
    path('logout', v.logout_view, name='logout')
    ]

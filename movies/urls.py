import sys
sys.path.append('..')

from django.urls import path

from . import views
from users import views as v



urlpatterns = [
    path('', views.index),
    path('<int:movie_id>', views.movie),
    path('', v.index, name='index'),
    path('login', v.login_view, name='login'),
    path('logout', v.logout_view, name='logout')
    ]

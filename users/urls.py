import sys
sys.path.append('..')

from django.urls import path

from . import views
from movies import views as v

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    path('movies', v.index, name='movies'),
    #path('signup', views.signup_view, name='signup')
]

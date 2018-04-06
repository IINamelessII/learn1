from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def index(request):
    if not request.user.is_authenticated:
        context = {
            'message':None
        }
        return render(request, 'users/login.html', context)
    context = {
        'user': request.user
    }
    return render(request, 'users/user.html', context)


def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('index'))
    else:
        context = {
            'message': 'Invalid try.'
        }
        return render(request, 'users/login.html', context)


def logout_view(request):
    logout(request)
    context = {
        'message': 'Logged out.'
    }
    return render(request, 'users/login.html', context)

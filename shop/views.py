from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Object


def index(request):
    #return HttpResponse('Here all')
    contex = {
        "categoryes": Category.objects.all()
    }
    return render(request, "shop/index.html", contex)

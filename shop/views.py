from django.shortcuts import render
from django.http import HttpResponse

from .models import Category, Subcategory


def index(request):
    contex = {
        "categoryes": Category.objects.all(),
        "subcategoryes": Subcategory.objects.all()
    }
    return render(request, "shop/index.html", contex)

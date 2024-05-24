# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def home__page(request):
    return render(request, "index.html")


# def check__about__page(request):
#     return render(request, "check/about.html")


def about__page(request):
    return render(request, "about.html")


# def product():
#     pass


# def product__list():
#     pass

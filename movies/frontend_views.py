from django.shortcuts import render
from .models import Movie
from django.contrib.auth.decorators import login_required


def home(request):
    movies = Movie.objects.all()

    return render(
        request,
        "home.html",
        {"movies": movies}
    )


def register_page(request):
    return render(request, "register.html")


def login_page(request):
    return render(request, "login.html")
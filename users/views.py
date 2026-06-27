from rest_framework import generics
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect

from .serializers import RegisterSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer


def logout_view(request):
    logout(request)
    return redirect("/")

from django.shortcuts import render

def login_page(request):
    return render(request, "login.html")
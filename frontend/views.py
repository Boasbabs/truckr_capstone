from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, "frontend/index.html", context={})


def login(request):
    return render(request, "frontend/login.html", context={})

def signup(request):
    return render(request, "frontend/signup.html", context={})
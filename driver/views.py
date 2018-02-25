from django.shortcuts import render
from django.views import generic


def index(request):
    return render(request, "driver/index.html", context={})


def login(request):
    return render(request, "driver/login.html", context={})


def signup(request):
    return render(request, "driver/signup.html", context={})
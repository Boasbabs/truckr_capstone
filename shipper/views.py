from django.shortcuts import render


def index(request):
    return render(request, "shipper/index.html", context={})


def login(request):
    return render(request, "shipper/login.html", context={})


def signup(request):
    return render(request, "shipper/signup.html", context={})

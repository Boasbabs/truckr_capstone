from django.shortcuts import render
from django.views import generic

# from driver.models import Driver


def index(request):
    return render(request, "driver/index.html", context={})


def login(request):
    return render(request, "driver/login.html", context={})


def signup(request):
    return render(request, "driver/signup.html", context={})


class DriverHomeView(generic.TemplateView):
    template_name = "driver/dashboard.html"
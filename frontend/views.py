from django.contrib.auth import login
from django.shortcuts import render, redirect, HttpResponse
from django.views import generic

from .models import User
from .forms import DriverSignUpForm, ShipperSignUpForm


def index(request):
    return render(request, "frontend/index.html", context={})


def login(request):
    return render(request, "frontend/login.html", context={})


class SignUpView(generic.TemplateView):
    template_name = "frontend/signup.html"

    # if request.method == 'POST':
    #     form = DriverSignUpForm(request.POST)
    #     if form.is_valid():
    #         pass  # does nothing, just trigger the validation
    # else:
    #     form = DriverSignUpForm()


class DriverSignUpView(generic.CreateView):
    """
    View for the driver signup form
    """
    model = User
    form_class = DriverSignUpForm
    template_name = "frontend/driver_signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "driver"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponse("Login !")


class ShipperSignUpView(generic.CreateView):
    """
    View for the Shipper to signup
    """
    model = User
    form_class = ShipperSignUpForm
    template_name = "frontend/shipper_signup_form.html"

    def get_context_data(self, **kwargs):
        kwargs["user_type"] = "shipper"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponse("Login shipper !")
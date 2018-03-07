from django.urls import path, include

from . import views


app_name = "frontend"
urlpatterns = [
    path("", views.index, name="index"),
    # path("login", views.login, name="login"),
    # # path("signup", views.signup, name="signup"),
    #
    # # path for the accounts signup
    # path('accounts/', include("allauth.urls")),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("signup/driver", views.DriverSignUpView.as_view(), name="driver_signup" ),
    path("signup/shipper", views.ShipperSignUpView.as_view(), name="shipper_signup" ),
]

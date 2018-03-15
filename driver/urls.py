from django.urls import path

from . import views


app_name = "driver"
urlpatterns = [
    # path("", views.index, name="index"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("", views.DriverRequestListView.as_view(), name="home"),
    path("detail", views.DriverRequestDetailView.as_view(), name="request_detail"),
    path("list", views.DriverRequestListView.as_view(), name="request_list"),
]

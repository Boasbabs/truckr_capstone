from django.urls import path

from . import views


app_name = "shipper"
urlpatterns = [
    path("", views.home, name="home"),
    path("order/create", views.CreateOrderView.as_view(), name="order_create"),
    path("order/list", views.OrderListView.as_view(), name="order_list"),
    path("order/detail", views.OrderDetailView.as_view(), name="order_detail"),
]

from django.urls import path

from . import views


app_name = "shipper"
urlpatterns = [
    path("", views.home, name="home"),
    path("order/create", views.CreateShipmentView.as_view(), name="order_create"),
    path("order/list", views.ShipmentListView.as_view(), name="order_list"),
    # path("order/detail", views.ShipmentDetailView.as_view(), name="order_detail"),
    path("order/detail/<int:pk>", views.ShipmentDetailView.as_view(), name="order_detail"),
]

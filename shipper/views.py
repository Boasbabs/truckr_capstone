from django.shortcuts import render
from django.views import generic


def home(request):
    return render(request, "shipper/index.html", context={})


class CreateOrderView(generic.TemplateView):
    template_name = "shipper/create_order.html"


class OrderDetailView(generic.TemplateView):
    template_name = "shipper/orderdetail.html"


class OrderListView(generic.TemplateView):
    template_name = "shipper/orderlist.html"

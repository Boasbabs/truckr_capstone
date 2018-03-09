from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import FormView, CreateView

from shipper.models import Shipment, Invoice
from shipper.forms import CreateShipmentForm


def home(request):
    return render(request, "shipper/create_order.html", context={})


class CreateShipmentView(CreateView):
    model = Shipment
    form = CreateShipmentForm()
    fields = "__all__"
    template_name = "shipper/create_order.html"
    success_url = reverse_lazy("shipper:order_detail")

    def post(self, request):
        if request.method == 'POST':
            form = CreateShipmentForm(request.POST)
            if form.is_valid():
                shipment = form.save(commit=False)
                shipment.shipper = request.user

                shipment.save()
                form.clean()

                # return super(CreateShipmentView, self).form_valid(form)
                return redirect("shipper:order_detail")
            else:
                return render(request, 'shipper/create_order.html',
                              {'form': form})
        else:
            form = CreateShipmentForm()
        return render_to_response('shipper/create_order.html', {'form': form},)


class ShipmentDetailView(generic.TemplateView):
    model = Shipment
    template_name = "shipper/orderdetail.html"


# class ShipmentDetailView(generic.DetailView):
#     model = Shipment
#     template_name = "shipper/orderdetail.html"
#
#     latest = Shipment.objects.all().latest("order_date")
#
#     def get_object(self, *args, **kwargs):
#         shipment = get_object_or_404(Shipment, pk=self.kwargs['pk'])
#         return shipment
#
#     def get_queryset(self):
#         """Filter pages by a book"""
#         return self.Shipment.objects.all().latest("order_date")


class ShipmentListView(generic.ListView):
    model = Shipment
    template_name = "shipper/orderlist.html"

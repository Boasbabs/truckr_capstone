from django.contrib import admin
from shipper.models import Shipment, Invoice
# Register your models here.


@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    pass

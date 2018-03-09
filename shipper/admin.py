from django.contrib import admin
from shipper.models import Shipment, Invoice
# Register your models here.

admin.site.register(Shipment)
admin.site.register(Invoice)

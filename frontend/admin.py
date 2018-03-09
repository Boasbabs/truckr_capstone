from django.contrib import admin

from .models import Driver, Shipper, Shipment, \
    DriverAddress, ShipperAddress, Truck, BankAccount

admin.site.register(Driver)
admin.site.register(DriverAddress)
admin.site.register(Shipper)
admin.site.register(ShipperAddress)
admin.site.register(Truck)
admin.site.register(Shipment)
admin.site.register(BankAccount)

import uuid
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from frontend.models import Shipper, User
# Shipper's Model


class Shipment(models.Model):
    """
    This is the order create when a load is need to be transfer
    """
    LOCATION = (
        ("accra", 'ACCRA'),
        ("kumasi", 'KUMASI'),
        ("tema", 'TEMA'),
        ("tamale", 'TAMALE'),
        ("tokoradi", 'SEKONDI-TAKORADI'),
        ("cape_coast", 'CAPE COAST'),
        ("teshie", 'TESHIE'),
        ("sunyani", 'SUNYANI'),
    )
    shipper = models.ForeignKey(User, on_delete=models.CASCADE,)
    order_number = models.UUIDField(default=uuid.uuid4, help_text="Unique ID for shipment order created")
    order_date = models.DateTimeField(auto_now=True)
    cargo_material = models.CharField(max_length=225)
    pickup_date = models.DateField(null=True, blank=True)
    cargo_weight = models.IntegerField()
    pickup_address = models.CharField(max_length=225)
    pickup_location = models.CharField(max_length=100, choices=LOCATION, default="accra", null=True, blank=True, help_text='Pickup Location')
    destination_address = models.CharField(max_length=225)
    destination_location = models.CharField(max_length=100, choices=LOCATION, default="tema", null=True, blank=True, help_text='Delivery Location')
    order_notes = models.TextField()
    matched_order_to = models.CharField(default=None, null=True, blank=True, max_length=55)

    class Meta:
        ordering = ["pickup_date"]
        verbose_name = 'shipment'
        verbose_name_plural = 'shipments'

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this book.
        """
        return reverse('shipper:order_detail',  kwargs={'pk': self.id})

    def __str__(self):
        """
        String for representing the Model object
        """
        return 'Shipment Order: {0} ({1})'.format(self.id, self.cargo_material)

    def get_latest(self):
        # now = timezone.now()
        latest = Shipment.objects.all().latest("order_date")
        return latest


class Invoice(models.Model):
    """
    This is the order create when a load is need to be transfer
    """
    STATUS = (
        ("UNPAID", 'unpaid'),
        ("PAID", 'paid'),
    )
    shipment = models.ForeignKey("Shipment", on_delete=models.CASCADE, blank=True, null=True)
    payment_status = models.CharField(max_length=15, choices=STATUS, blank=True, null=True)
    amount = models.IntegerField()

    def __str__(self):
        """
        String for representing the Model object
        """
        return 'Invoice: {0} ({1})'.format(self.amount, self.payment_status)
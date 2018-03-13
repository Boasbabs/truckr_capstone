import uuid
from django.db import models
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.db.models.signals import post_save

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


# signal gets triggered when shipment order is created.
def check_matched_order(sender, **kwargs):
    if kwargs['created']:
        is_matched_order()

post_save.connect(check_matched_order, sender=Shipment)


def is_matched_order():
    """
    This is the function that checks for matched order.
    :return:
    """
    latest = Shipment.objects.latest('order_date')

    #for converting string to string
    #print("".join([p.pickup_location for p in match]))

    #query for match
    check_for_match = Shipment.objects.all().filter(
        destination_location=latest.pickup_location
    ).filter(
        pickup_location=latest.destination_location
    )

    if check_for_match:
        for p in check_for_match:
            p.matched_order_to = latest.id
            latest.matched_order_to = p.id
            latest.save()
            p.save()

    return check_for_match


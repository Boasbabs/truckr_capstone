"""
Insight from https://simpleisbetterthancomplex.com/ to Implement Multiple User Types
"""

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.urls import reverse


class User(AbstractBaseUser):
    """
    Extended the User model for the two users, driver and shipper
    """
    email = models.EmailField(max_length=100, unique=True)

    USERNAME_FIELD = 'email'
    is_driver = models.BooleanField(default=False)
    is_shipper = models.BooleanField(default=False)


class Driver(models.Model):
    """
    The model for driver who can drive the truck and get notification of order.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    full_name = models.CharField(max_length=50, default="full name")
    phone_number = models.CharField(max_length=20, unique=True)
    driver_license = models.CharField(max_length=15, unique=True)
    join_date = models.DateTimeField(auto_now=True)

    # META CLASS
    class Meta:
        verbose_name = 'driver'
        verbose_name_plural = 'drivers'

    # TO STRING METHOD
    def __str__(self):
        return "Driver: {0}".format(self.full_name,)

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('driver_details', kwargs={'pk': self.id})


class Shipper(models.Model):
    """
    The model for the one who wants to send shipments/load
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    owner_name = models.CharField(max_length=50, default="owner name")
    company_name = models.CharField(max_length=50, default="company name")
    phone_number = models.CharField(max_length=20, unique=True)
    join_date = models.DateTimeField(auto_now=True)

    # META CLASS
    class Meta:
        verbose_name = 'shipper'
        verbose_name_plural = 'shippers'

    # TO STRING METHOD
    def __str__(self):
        return "Shipper: {0}".format(self.company_name)

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('shipper_details', kwargs={'pk': self.id})


class DriverAddress(models.Model):
    """
    This stores the driver's address
    """
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE, related_name='drivers')
    street = models.CharField(max_length=70)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    # META CLASS
    class Meta:
        verbose_name = 'driver address'

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('driver_address_details', kwargs={'pk': self.id})


class ShipperAddress(models.Model):
    """
    This stores the company address
    """
    shipper = models.ForeignKey(Shipper, on_delete=models.CASCADE, related_name='shippers')
    street = models.CharField(max_length=70)
    city = models.CharField(max_length=20)
    country = models.CharField(max_length=20)

    # META CLASS
    class Meta:
        verbose_name = 'shipper address'

    # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('shipper_address_details', kwargs={'pk': self.id})


class Shipment(models.Model):
    """
    The model for orders of shipments/load that wants to be transfered
    """
    pass


class Truck(models.Model):
    """
    The model for trucks driven by drivers
    """
    pass


class BankAccount(models.Model):
    """
    The bank details for transaction on the shipper and drivers end
    """
    pass
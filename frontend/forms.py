from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.utils.translation import ugettext_lazy as _

from .models import Driver, Shipper, User


class DriverSignUpForm(UserCreationForm):
    """
    Driver's signup form
    """
    first_name = forms.CharField(label='Your Name', max_length=30, required=True)
    last_name = forms.CharField(label='Your Surname', max_length=30, required=True)
    phone_number = forms.IntegerField(required=True)
    driver_license = forms.CharField(max_length=15)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "first_name",
            "last_name",
            "phone_number",
            "driver_license",
        ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.save()
        driver = Driver.objects.create(user=user)
        driver.first_name.add(*self.cleaned_data.get("first_name"))
        return user

    def clean(self):
        cleaned_data = super(DriverSignUpForm, self).clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')
        phone_number = cleaned_data.get('phone_number')
        if not first_name and not last_name and not phone_number:
            raise forms.ValidationError('You have to write something!')


class ShipperSignUpForm(UserCreationForm):
    """
    The signup form for Shipper
    """
    class Meta(UserCreationForm.Meta):
        model = User


    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_shipper = True
        if commit:
            user.save()
        return user
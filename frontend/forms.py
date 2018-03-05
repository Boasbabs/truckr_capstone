from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import Driver, Shipper, User


class DriverSignUpForm(UserCreationForm):
    """
    Driver's signup form
    """
    email = forms.EmailField(label='Your Email', max_length=100, required=True)
    full_name = forms.CharField(max_length=50, required=True)
    phone_number = forms.CharField(required=True)
    driver_license = forms.CharField(max_length=15)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "email",
            "full_name",
            "phone_number",
            "driver_license",
        ]

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_driver = True
        user.save()
        return Driver.objects.create(user=user,
                                     full_name=self.cleaned_data.get('full_name'),
                                     phone_number=self.cleaned_data.get('phone_number'),
                                     driver_license=self.cleaned_data.get('driver_license')
                                     )

    def clean(self):
        cleaned_data = super(DriverSignUpForm, self).clean()
        full_name = cleaned_data.get('full_name')
        phone_number = cleaned_data.get('phone_number')
        driver_license = cleaned_data.get('driver_license')
        if not full_name and not phone_number and not driver_license:
            raise forms.ValidationError('You have to write something!')


class ShipperSignUpForm(UserCreationForm):
    """
    The signup form for Shipper
    """
    email = forms.EmailField(max_length=100, required=True)
    owner_name = forms.CharField(label="Owner\'s Name", max_length=50, required=True)
    company_name = forms.CharField(label='Your Company Name', max_length=50, required=True)
    phone_number = forms.CharField(max_length=20, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = [
            "email",
            "owner_name",
            "company_name",
            "phone_number",
        ]

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_shipper = True
        if commit:
            user.save()
        return Shipper.objects.create(user=user,

                                     owner_name=self.cleaned_data.get('owner_name'),
                                     company_name=self.cleaned_data.get('company_name'),
                                     phone_number=self.cleaned_data.get('phone_number'),
                                     )

import datetime
from django import forms
from shipper.models import Shipment


class CreateShipmentForm(forms.ModelForm):
    """
    Form class for creating shipment
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
    # order_date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"))
    cargo_material = forms.CharField(max_length=100)
    pickup_date = forms.DateField(widget=forms.widgets.DateInput(format="%m/%d/%Y"),)
    cargo_weight = forms.IntegerField(label="Cargo Weight (in tonnes)", help_text="Weight in tonnes")
    pickup_address = forms.CharField(label="Pickup Address", max_length=225)
    pickup_location = forms.ChoiceField(label="Pickup Location", choices=LOCATION, widget=forms.Select())
    destination_address = forms.CharField(label="Destination Address", max_length=225)
    destination_location = forms.ChoiceField(label="Destination Location", choices=LOCATION)
    order_notes = forms.CharField(
        max_length=2000,
        label="Additional Shippment Details",
        widget=forms.Textarea(),
        help_text='Other details here!',
    )

    class Meta:
        model = Shipment
        # fields = "__all__"
        exclude = ('shipper', 'order_number',)

        # to ensure that pass dates are not submitted
    def clean_date(self):
        date = self.cleaned_data['date']
        if date < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return date

    def clean(self):
        cleaned_data = super(CreateShipmentForm, self).clean()
        cargo_material = cleaned_data.get('cargo_material')
        pickup_date = cleaned_data.get('pickup_date')
        cargo_weight = cleaned_data.get('cargo_weight')
        pickup_address = cleaned_data.get('pickup_address')
        pickup_location = cleaned_data.get('pickup_location')
        destination_address = cleaned_data.get('destination_address')
        destination_location = cleaned_data.get('destination_location')
        order_notes = cleaned_data.get(' order_notes')
        if not cargo_material and not pickup_location and not destination_location:
            raise forms.ValidationError('You have to write something!')




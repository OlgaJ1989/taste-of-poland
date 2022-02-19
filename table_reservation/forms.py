""" File specyfying implemented forms and their settings. """
from django.forms import ModelForm, widgets
from .models import Reservation


class ReservationForm(ModelForm):
    """ Data for the table booking model form and widgets to be displayed. """
    class Meta:
        """ Meta class specifying fields and widgets to be displayed. """
        model = Reservation
        fields = ('first_name', 'last_name', 'party_size',
                  'date', 'time', 'table', 'additional_info')
        widgets = {
            'date': widgets.SelectDateWidget(
                years=range(2022, 2024), empty_label=("Year", "Month", "Day"))
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['party_size'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['date'].widget.attrs.update(
            {'class': 'form-control date-picker'})
        self.fields['time'].widget.attrs.update({'class': 'form-control'})
        self.fields['table'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['additional_info'].widget.attrs.update(
            {'class': 'form-control', 'rows': '3', 'placeholder':
             'Is there anything else we need to know? Tell us!'})

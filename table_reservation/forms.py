from django.forms import ModelForm, widgets
from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('first_name', 'last_name', 'party_size',
                  'date', 'time', 'additional_info')
        widgets = {
            'date': widgets.SelectDateWidget(
                empty_label=("Year", "Month", "Day"))
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['party_size'].widget.attrs.update(
            {'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control'})
        self.fields['time'].widget.attrs.update({'class': 'form-control'})
        self.fields['additional_info'].widget.attrs.update(
            {'class': 'form-control'})

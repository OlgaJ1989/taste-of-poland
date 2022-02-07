from django.forms import ModelForm, widgets
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ('first_name', 'last_name', 'party_size',
                  'date', 'time', 'additional_info')
        widgets = {
            'date': widgets.SelectDateWidget(years=range(2022, 2024), empty_label=("Year", "Month", "Day"))
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['party_size'].widget.attrs.update({'class': 'form-control'})
        self.fields['date'].widget.attrs.update({'class': 'form-control date-picker'})
        self.fields['time'].widget.attrs.update({'class': 'form-control'})
        self.fields['additional_info'].widget.attrs.update({'class': 'form-control', 'rows': '3'})

        def validate_min(value):
            if value < 1 or value > 4:
                raise ValidationError(
                    _('Please choose between 1 and 4 people.'),
                    params={'value': value},
                )

        self.fields['party_size'].validators = [validate_min]

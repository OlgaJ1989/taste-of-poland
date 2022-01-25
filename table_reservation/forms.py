from django.forms import ModelForm, widgets
from .models import Reservation


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"
        widgets = {'date': widgets.SelectDateWidget(
            empty_label=("Year", "Month", "Day"))}

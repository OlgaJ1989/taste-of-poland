from django.shortcuts import render
from .forms import ReservationForm


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def create_booking(request):
    form = ReservationForm()
    context = {'form': form}
    return render(request, 'booking_form.html', context)

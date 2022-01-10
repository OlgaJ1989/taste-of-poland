from django.shortcuts import render, redirect
from .forms import ReservationForm


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def create_booking(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'booking_form.html', context)

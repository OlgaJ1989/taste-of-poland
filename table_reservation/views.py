from django.shortcuts import render, redirect
from .forms import ReservationForm
from .models import Reservation


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def gallery(request):
    return render(request, 'gallery.html')


def profile(request):
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'profile.html', context)


def booking_details(request, pk):
    reservation = Reservation.objects.get(id=pk)
    return render(request, 'booking_details.html')


def create_booking(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'booking_form.html', context)


def update_booking(request, pk):
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation)
    if request.method == 'POST':
        form = ReservationForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'booking_form.html', context)


def delete_booking(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.method == 'POST':
        reservation.delete()
        return redirect('profile')
    return render(request, 'delete.html', {'obj': reservation})

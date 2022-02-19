"""
File specyfying what views can be found in the app.
"""
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation


def home(request):
    """
    View generating the Home page template.
    """
    return render(request, 'index.html')


def menu(request):
    """
    View generating the Menu template.
    """
    return render(request, 'menu.html')


def gallery(request):
    """
    View generating the Gallery template.
    """
    return render(request, 'gallery.html')


def contact(request):
    """
    View generating the Contact page template.
    """
    return render(request, 'contact.html')


def page_404(request):
    """
    View generating the 404 error page template.
    """
    return render(request, '404.html')


def profile(request):
    """
    View generating the Profile (Current Bookings) template.
    """
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'profile.html', context)


@login_required(login_url='account_login')
def create_booking(request):
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.booker = request.user
            form.save()
            return redirect('profile')
    context = {'form': form}
    return render(request, 'booking_form.html', context)


@login_required(login_url='account_login')
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


@login_required(login_url='account_login')
def delete_booking(request, pk):
    reservation = Reservation.objects.get(id=pk)
    if request.user == reservation.booker:
        if request.method == 'POST':
            reservation.delete()
            return redirect('profile')
        return render(request, 'delete.html', {'obj': reservation})

        # else

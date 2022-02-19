""" File specyfying what views can be found in the app. """
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation


def home(request):
    """ View generating the Home page. """
    return render(request, 'index.html')


def menu(request):
    """ View generating the Menu page. """
    return render(request, 'menu.html')


def gallery(request):
    """ View generating the Gallery page. """
    return render(request, 'gallery.html')


def contact(request):
    """ View generating the Contact page. """
    return render(request, 'contact.html')


def page_404(request):
    """ View generating the 404 error page. """
    return render(request, '404.html')


def profile(request):
    """ View generating the Profile (Current Bookings) page. """
    reservations = Reservation.objects.all()
    context = {'reservations': reservations}
    return render(request, 'profile.html', context)


@login_required(login_url='account_login')
def create_booking(request):
    """ View allowing users to login. """
    form = ReservationForm()
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.booker = request.user
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "Booking created successfully.")
            return redirect('profile')
    context = {'form': form}
    return render(request, 'booking_form.html', context)


@login_required(login_url='account_login')
def update_booking(request, pk):
    """ View allowing users do modify existing bookings. """
    reservation = Reservation.objects.get(id=pk)
    form = ReservationForm(instance=reservation)
    if request.user == reservation.booker:
        if request.method == 'POST':
            form = ReservationForm(request.POST, instance=reservation)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, "Your \
                    changes have been saved.")
                return redirect('profile')
        context = {'form': form}
        return render(request, 'booking_form.html', context)
    else:
        messages.add_message(
            request, messages.ERROR, "You are not authorised to edit \
                this reservation.")
        return redirect('profile')


@login_required(login_url='account_login')
def delete_booking(request, pk):
    """ View allowing users to delete existing bookings. """
    reservation = Reservation.objects.get(id=pk)
    if request.user == reservation.booker:
        if request.method == 'POST':
            reservation.delete()
            messages.add_message(request, messages.SUCCESS, "Booking deleted.")
            return redirect('profile')
        return render(request, 'delete.html', {'obj': reservation})
    else:
        messages.add_message(
            request, messages.ERROR, "You are not authorised to delete \
                this reservation.")
        return redirect('profile')

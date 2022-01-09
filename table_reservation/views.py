from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')


def create_booking(request):
    context = {}
    return render(request, 'booking_form.html', context)

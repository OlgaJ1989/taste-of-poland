from django.shortcuts import render


def home(request):
    return render(request, 'table_reservation/index.html')
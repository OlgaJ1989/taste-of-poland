from django.shortcuts import render


def say_hello(request):
    return render(request, 'table_reservation/index.html')
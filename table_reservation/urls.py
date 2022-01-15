from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('create-booking', views.create_booking, name="create-booking"),
    path('profile/', views.profile, name="profile"),
    path('booking_details/<str:pk>/', views.booking_details, name="booking_details"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('profile/', views.profile, name="profile"),
    path('booking_details/<str:pk>/', views.booking_details, name="booking_details"),
    path('create-booking', views.create_booking, name="create-booking"),
    path('update-booking/<str:pk>/', views.update_booking, name="update-booking"),
    path('delete-booking/<str:pk>/', views.delete_booking, name="delete-booking"),
]

from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', views.menu, name="menu"),
    path('gallery/', views.gallery, name="gallery"),
    path('contact/', views.contact, name="contact"),
    path('profile/', views.profile, name="profile"),
    path('404/', views.page_404, name="404"),
    path('create-booking', views.create_booking, name="create-booking"),
    path('update-booking/<str:pk>/', views.update_booking, name="update-booking"),
    path('delete-booking/<str:pk>/', views.delete_booking, name="delete-booking"),
]

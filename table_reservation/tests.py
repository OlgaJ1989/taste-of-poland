""" Automated testing """
from django.test import TestCase
from django.urls import resolve, reverse
from .views import (
    home, menu, gallery, contact, page_404, profile, create_booking,
    update_booking, delete_booking)


class TestUrls(TestCase):
    """ Test urls.py """

    def test_home_url_renders_home_view(self):
        """ Test 'home' url is working and rendering 'home' view. """
        url = reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

    def test_menu_url_renders_menu_view(self):
        """ Test 'menu' url is working and rendering 'menu' view. """
        url = reverse('menu')
        print(resolve(url))
        self.assertEqual(resolve(url).func, menu)

    def test_gallery_url_renders_gallery_view(self):
        """ Test 'gallery' url is working and rendering 'gallery' view. """
        url = reverse('gallery')
        print(resolve(url))
        self.assertEqual(resolve(url).func, gallery)

    def test_contact_url_renders_contact_view(self):
        """ Test 'contact' url is working and rendering 'contact' view. """
        url = reverse('contact')
        print(resolve(url))
        self.assertEqual(resolve(url).func, contact)

    def test_404_url_renders_page_404_view(self):
        """ Test 'contact' url is working and rendering 'page_404' view. """
        url = reverse('404')
        print(resolve(url))
        self.assertEqual(resolve(url).func, page_404)

    def test_profile_url_renders_profile_view(self):
        """ Test 'contact' url is working and rendering 'profile' view. """
        url = reverse('profile')
        print(resolve(url))
        self.assertEqual(resolve(url).func, profile)

    def test_create_booking_url_renders_create_booking_view(self):
        """ Test 'create-booking' url renders 'profile' view. """
        url = reverse('create-booking')
        print(resolve(url))
        self.assertEqual(resolve(url).func, create_booking)

    def test_update_booking_url_renders_update_booking_view(self):
        """ Test 'update-booking' url renders 'update_booking' view. """
        url = reverse('update-booking', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, update_booking)

    def test_delete_booking_url_renders_delete_booking_view(self):
        """ Test 'delete-booking' url renders 'delete_booking' view. """
        url = reverse('delete-booking', args=[20])
        print(resolve(url))
        self.assertEqual(resolve(url).func, delete_booking)


class TestViews(TestCase):
    """ Test views.py """

    def test_booking_form_redirects_when_not_logged_in(self):
        """ Test 'Reserve a room' redirects when not logged in. """
        response = self.client.get('/create-booking')
        self.assertEqual(response.status_code, 302)

    def test_login_redirects_to_home_page(self):
        """ Test when login successful redirected to home page' """
        self.client.login(username='Test', password='Test12345')  
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

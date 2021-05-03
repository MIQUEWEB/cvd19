from django.test import TestCase
from django.http import HttpRequest
from django.urls import resolve
from RICList.views import HomePage
#from django.http import HttpResponse
from django.template.loader import render_to_string



class HomePageTest(TestCase):
	def test_root_url_resolves_to_home_page_views(self):
		found = resolve('/')
		self.assertEqual(found.func, home_page)
	def test_homepage_return_correct_html(self):
		request = HttpRequest()
		response = HomePage(request)
		expected_html = render_to_string('homepage.html')
		self.assertEqual(html,expected_html)
	def test_save_POST_request(self):
		response = self.client.post('/', data={'flname':'aaddress'})
		self.assertIn('fname', response.content.decode())
	
		#request = HttpRequest()
		#response = home_page(request)
		#self.assertTrue(response.content.startswith(b'<html>'))
		#self.assertIn(b'<title>Kdrama Suggest</title>',response.cdpp1025
		
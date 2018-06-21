from django.test import TestCase
from django.urls import reverse
from .views import index
from .forms import *

def createForm():
	form = SiteForm()
	return form

class encodingViewsTests(TestCase):
	def testIndex(self):
		form = createForm()
		reponse = self.client.get("/index")
		self.assertEqual(reponse.status_code, 200)

	def testIndexPost(self):
		form = SiteForm()
		reponse = self.client.post("/index")
		self.assertEqual(reponse.status_code,200)

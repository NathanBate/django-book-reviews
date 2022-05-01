from http import client
from django.test import TestCase
from django.test.utils import setup_test_environment
from django.test.client import Client

from .models import Review

def ReviewViewsTest(TestCase):
    client = Client()
    response = client.get('/')

# Create your tests here.

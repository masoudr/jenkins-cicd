from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
import json
# Create your tests here.

class TestUser(APITestCase):
    def test_user(self):
        data = {"name": "Masoud"}
        response = self.client.post('', data=data)
        data = json.loads(response.content.decode())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data["name"], "Masoud")
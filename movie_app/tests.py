from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CategoryModel, AuthorModel,MovieModel
import json

class MovieTest(APITestCase):
    def test_movie(self):
        # Register and login user to get token
        data = {'username': 'test1', 'password': 'test1', 'fullname': 'testname'}
        url = reverse('auth-register')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        data = {'username': 'test1', 'password': 'test1'}
        url = reverse('auth-login')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res_data = response.json()
        token = res_data['token']
        print("Token:", token)

        # add data
        category = CategoryModel.objects.create(name="Action")
        author = AuthorModel.objects.create(name="mher")
        MovieModel.objects.create(
            name="Test",
            description="powerfull banana",
            author=author,
            category=category
        )

        # Get movie list
        url = reverse('movie-list') + "?name=Test"  # Adjust the name filter if needed
        print(url)
        response = self.client.get(url, HTTP_AUTHORIZATION='Token ' + token)
        print(response)
        res_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print("Movie list:", res_data)
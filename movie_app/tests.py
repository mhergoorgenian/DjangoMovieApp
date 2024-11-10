from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CategoryModel, AuthorModel, MovieModel
from .serializers import MovieSerializer
import json

class MovieTest(APITestCase):
    def test_movie(self):
        # Register and login user to get token
        data = {'username': 'test1', 'password': 'test1', 'fullname': 'testname'}
        url = reverse('auth-register')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        
        # Login and get token
        data = {'username': 'test1', 'password': 'test1'}
        url = reverse('auth-login')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res_data = response.json()
        token = res_data['token']

        # Add data
        category = CategoryModel.objects.create(name="Action")
        author = AuthorModel.objects.create(name="mher")
        movie = MovieModel.objects.create(
            name="Test",
            description="powerful banana",
            author=author,
            category=category
        )
        
        # Expected data
        expected_data = {
            "data": [
                {
                    "name": "Test",
                    "description": "powerful banana",
                    "author": "mher",
                    "category": "Action",
                    "release_date": None,
                    "rating": None,
                    "duration": None
                }
            ],
            'total': 1
        }

        # Get movie list with filter
        url = reverse('movie-list') + "?name=Test"  # Adjust filter as needed
        response = self.client.get(url, HTTP_AUTHORIZATION='Token ' + token)
        res_data = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res_data, expected_data)

        # Additional test: No movies found
        url = reverse('movie-list') + "?name=NonExistentMovie"
        response = self.client.get(url, HTTP_AUTHORIZATION='Token ' + token)
        res_data = json.loads(response.content)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(res_data, {"data": [], "total": 0})

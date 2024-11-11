from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import MovieModel, AuthorModel, CategoryModel
from .serializers import MovieSerializer
import json

class MovieTest(APITestCase):
    def test_movie(self):
        #register login token
        user_data = {'username': 'testuser', 'password': 'testpassword'}
        register_url = reverse('auth-register')
        self.client.post(register_url, {**user_data, 'fullname': 'testname'})

        login_url = reverse('auth-login')
        response = self.client.post(login_url, user_data)
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

        # create db data
        self.category = CategoryModel.objects.create(name="Drama")
        self.author = AuthorModel.objects.create(name="John Doe")
        self.movie = MovieModel.objects.create(
            name="Test Movie",
            description="Test Description",
            author=self.author,
            category=self.category
        )
        print({"movie":MovieSerializer(self.movie).data})


        test_data ={'data':[
            {
            "name": "Test Movie",
            "description": "Test Description",
            "author": self.author.name,
            "category": self.category.name,
            "release_date":None,
            "rating":None,
            "duration":None
        }
        ],
        'total': 1
        }
        print({"movie":test_data})
        # test movie with filter
        movie_list_url = reverse('movie-list') + "?name=Test"
        response = self.client.get(movie_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print({"movie":response.content})
        self.assertEqual(response.data, test_data)
        
        # test movie creation
        movie_data = {
            "name": "New Movie",
            "description": "Description of new movie",
            "author": self.author.id,
            "category": self.category.id
        }
        response = self.client.post(reverse('movie-list'), data=movie_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print(response.content)
        
        # test movie by id
        movie_detail_url = reverse('movie-id', args=[self.movie.id])
        response = self.client.get(movie_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Test Movie")
        print(response.content)

        # movie update by id
        response = self.client.put(movie_detail_url, {"name": "Updated Movie"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Movie")
        print(response.content)

        # movie deletion by id
        response = self.client.delete(movie_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print(response.content)

        # author creation
        author_data = {"name": "New Author"}
        author_list_url = reverse('author-list')
        response = self.client.post(author_list_url, data=author_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Author")
        print(response.content)

        # category creation
        category_data = {"name": "New Category"}
        category_list_url = reverse('category-list')
        response = self.client.post(category_list_url, data=category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], "New Category")
        print(response.content)

        # test author by id, update, and delete
        author_detail_url = reverse('author-id', args=[self.author.id])
        response = self.client.get(author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.content)
        
        response = self.client.put(author_detail_url, {"name": "Updated Author"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Author")
        print(response.content)

        response = self.client.delete(author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print(response.content)

        # test category by id, update, and delete
        category_detail_url = reverse('category-id', args=[self.category.id])
        response = self.client.get(category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.content)
        
        response = self.client.put(category_detail_url, {"name": "Updated Category"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Category")
        print(response.content)

        response = self.client.delete(category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        print(response.content)

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import MovieModel, AuthorModel, CategoryModel
from auth_app.models import ProfileModel
from django.contrib.auth.models import User
class MovieTest(APITestCase):

    def setUp(self):
        # Register and login to get the authorization token
        #user_data = {'username': 'testuser', 'password': 'testpassword'}
        #register_url = reverse('auth-register')
        #self.client.post(register_url, {**user_data, 'fullname': 'testname'})
        
        #create superuser
        self.superuser = User.objects.create_superuser(
            username='adminuser',
            password='superpassword',
            email='admin@example.com'
        )
        
        #login
        login_url = reverse('auth-login')
        response = self.client.post(login_url, {'username': 'adminuser', 'password': 'superpassword'})
        
        #token
        token = response.data['token']
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token)

    # Category CRUD
    def test_category_crud(self):
        # Create category
        category_data = {"name": "Drama"}
        category_list_url = reverse('category-list')
        response = self.client.post(category_list_url, data=category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        category_id = response.data['id']

        # Get category list
        category_get_list_url = reverse('category-list')
        response = self.client.get(category_get_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data['data'])
        data=[
            {
                "id":1,
                "name":"Drama"
            }
        ]
        self.assertEqual(response.data['data'], data)
        
        
        # Retrieve category by ID
        category_detail_url = reverse('category-id', args=[category_id])
        response = self.client.get(category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Drama")

        # Update category by ID
        updated_data = {"name": "Updated Drama"}
        response = self.client.put(category_detail_url, data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated Drama")

        # Delete category by ID
        response = self.client.delete(category_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Author CRUD
    def test_author_crud(self):
        # Create author
        author_data = {"name": "John Doe"}
        author_list_url = reverse('author-list')
        response = self.client.post(author_list_url, data=author_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author_id = response.data['id']


        # Get author list
        author_get_list_url = reverse('author-list')
        response = self.client.get(author_get_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data['data'])
        data=[
            {
                "id":1,
                "name":"John Doe",
                "bio": None
            }
        ]
        self.assertEqual(response.data['data'], data)
        
        # Retrieve author by ID
        author_detail_url = reverse('author-id', args=[author_id])
        response = self.client.get(author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "John Doe")

        # Update author by ID
        updated_data = {"name": "Updated John Doe"}
        response = self.client.put(author_detail_url, data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated John Doe")

        # Delete author by ID
        response = self.client.delete(author_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    # Movie CRUD
    def test_movie_crud(self):

        #create category
        category_data = {"name": "Drama"}
        category_list_url = reverse('category-list')
        response = self.client.post(category_list_url, data=category_data)
        category_id = response.data['id']
        category_name=response.data['name']
        print(response.data)

        #create author
        author_data = {"name": "John Doe"}
        author_list_url = reverse('author-list')
        response = self.client.post(author_list_url, data=author_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        author_id = response.data['id']
        author_name=response.data['name']
        print({"response":response.data})

        #create movie
        create_url = reverse('movie-list')  # Ensure this matches your URL configuration
        create_data = {
            "name": "Test Movie",
            "description": "A test movie description.",
            "category": category_id,
            "author": author_id
        }
        response = self.client.post(create_url, data=create_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        print({"response":response.data})
        movie_id=response.data['id']

        # Get movie list
        movie_get_list_url = reverse('movie-list')
        response = self.client.get(movie_get_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data['data'])
        data=[
            {
                'name': 'Test Movie',
                'description': 'A test movie description.',
                'author': 'John Doe',
                'category': 'Drama',
                'release_date': None,
                'rating': None,
                'duration': None
            }
        ]
        print(data)
        self.assertEqual(response.data['data'], data)
        print(response.content)
        
        

        # Retrieve movie by ID
        testdata={
                'name': 'Test Movie',
                'description': 'A test movie description.',
                'author': 'John Doe',
                'category': 'Drama',
                'release_date': None,
                'rating': None,
                'duration': None
        }
        movie_detail_url = reverse('movie-id', args=[movie_id])
        response = self.client.get(movie_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print({"Id":response.data})
        print({"Id":data})
        self.assertEqual(response.data,testdata)

        # Update Movie by ID
        updated_data = {"name": "Updated John Doe"}
        response = self.client.put(movie_detail_url, data=updated_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], "Updated John Doe")
        print({"Update":response.data})

        # Delete Movie by ID
        response = self.client.delete(movie_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)







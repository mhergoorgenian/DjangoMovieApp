from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
import json

class ProfileTest(APITestCase):
    def test_auth(self):

        #register
        data={'username':'test1','password':'test1','fullname':'testname'}
        url = reverse('auth-register')
        response = self.client.post(url, data, format='json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        res_data = response.json()
        self.assertIn('data', res_data)


        #login
        data={'username':'test1','password':'test1'}
        url = reverse('auth-login')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        res_data = response.json()
        print(res_data)
        token=res_data['token']
        print(token)



        #me

        url = reverse('get-mydata')
        response = self.client.get(url, HTTP_AUTHORIZATION='Token ' + token)
        res_data = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(res_data)
       
    


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from .models import ProfileModel
from .serializers import UserSerializer,ProfileSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAdminUser
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework import status



class MeView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request:Request):
        
        try: 
            user_profile = ProfileModel.objects.get(user=request.user)
            serializer = ProfileSerializer(user_profile)
            return Response({"data": serializer.data}, status=status.HTTP_200_OK)
        
        except Exception as e:
            return Response(
                {"error": f"An unexpected error occurred: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        

class RegisterView(APIView):
    permission_classes = []
    def post(self,request:Request):
        username=request.data.get('username')
        password=request.data.get('password')
        fullname=request.data.get('fullname')

        try:
            user=User.objects.filter(username=username)
            if user:
                Response({"error": {"message": "User already exists"}}, status=400)
            user = User(username=username)
            user.set_password(password)
            user.save()
            
            
            profile = ProfileModel.objects.create(user=user,fullname=fullname)
            data = ProfileSerializer(profile).data
            return Response({"data": data}, status=201)
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)


        

class LoginView(APIView):
    permission_classes = []
    def post(self,request:Request):
        username=request.data.get('username')
        password=request.data.get('password')

        try:
            user = authenticate(username=username, password=password)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key})
            else:
                return Response({ "error" : {"message"  : "Invalid username or password"} },status=400)
            
        except Exception as e:
            return Response({"message": str(e)}, status=status.HTTP_400_BAD_REQUEST)   

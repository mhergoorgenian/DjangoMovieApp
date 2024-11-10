from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from .models import MovieModel,CategoryModel,AuthorModel
from .serializers import MovieSerializer,AuthorSerializer,CategorySerializer
from django.shortcuts import get_object_or_404

class MovieView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request:Request):
        name=request.query_params.get('name')
        category=request.query_params.get('category')
        author=request.query_params.get('author')
        offset=request.query_params.get('offset',0)
        limit=request.query_params.get('limit',5)
        if name:
            total=MovieModel.objects.filter(name__startswith=name).count()
            movies=MovieModel.objects.filter(name__startswith=name)[offset:limit]
        elif category:
            total=MovieModel.objects.filter(category__startswith=category).count()
            movies=MovieModel.objects.filter(category__startswith=category)[offset:limit]
        elif author:
            total=MovieModel.objects.filter(author__startswith=author).count()
            movies=MovieModel.objects.filter(author__startswith=author)[offset:limit]
        else:
            total=MovieModel.objects.all().count()
            movies=MovieModel.objects.all()[offset:limit]
        serializer = MovieSerializer(movies, many=True)
        return Response({'data': serializer.data,'total':total})
    
class MovieDetailView(APIView):
    def get(self, request, id):
        movie = get_object_or_404(MovieModel, id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
        

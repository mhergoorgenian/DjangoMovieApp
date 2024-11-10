from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework import status
from .models import MovieModel,CategoryModel,AuthorModel
from .serializers import MovieSerializer,AuthorSerializer,CategorySerializer,MovieCreateSerializer
from django.shortcuts import get_object_or_404

class MovieView(APIView):

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
    

            

class MovieDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def delete(self, request, id):
        movie = get_object_or_404(MovieModel, id=id)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


class MovieCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def post(self, request):
        serializer = MovieCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieUpdateView(APIView):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]

    def put(self, request, id):
        movie = get_object_or_404(MovieModel, id=id)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class MovieDetailView(APIView):
    def get(self, request, id):
        movie = get_object_or_404(MovieModel, id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
class CategoryView(APIView):
    def get(self, request):
        categories = CategoryModel.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

class AuthorView(APIView):
    def get(self, request):
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

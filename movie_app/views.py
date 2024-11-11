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
    
    
    
    def post(self, request):
        serializer = MovieCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    
class MovieDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request:Request, id):
        movie = get_object_or_404(MovieModel, id=id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request:Request, id):
        movie = get_object_or_404(MovieModel, id=id)
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
        
    
    def delete(self, request:Request, id):
        movie = get_object_or_404(MovieModel, id=id)
        movie.delete()
        return Response({'message': 'Movie deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    


class AuthorView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request: Request):
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', 5))
        authors = AuthorModel.objects.all()[offset:limit]
        total = AuthorModel.objects.all().count()
        serializer = AuthorSerializer(authors, many=True)
        return Response({'data': serializer.data, 'total': total})

    def post(self, request):
        serializer = AuthorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    

class AuthorDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request:Request, id):
        author = AuthorModel.objects.get(pk=id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

    def put(self, request:Request, id):
        author = AuthorModel.objects.get(pk=id)
        serializer = AuthorSerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    def delete(self, request:Request, id):
        author = AuthorModel.objects.get(pk=id)
        if author:
            author.delete()
            return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error: Author Not Found"}, status=status.HTTP_403_FORBIDDEN)
        



class CategoryView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request: Request):
        offset = int(request.query_params.get('offset', 0))
        limit = int(request.query_params.get('limit', 5))
        categories = CategoryModel.objects.all()[offset:limit]
        total = CategoryModel.objects.all().count()
        serializer = CategorySerializer(categories, many=True)
        return Response({'data': serializer.data, 'total': total})

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


        
class CategoryDetailView(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request:Request, id):
        author = CategoryModel.objects.get(pk=id)
        serializer = CategorySerializer(author)
        return Response(serializer.data)

    def put(self, request:Request, id):
        author = CategoryModel.objects.get(pk=id)
        serializer = CategorySerializer(author, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    
    def delete(self, request:Request, id):
        author = CategoryModel.objects.get(pk=id)
        if author:
            author.delete()
            return Response({"detail": "Deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error: Author Not Found"}, status=status.HTTP_403_FORBIDDEN)
        
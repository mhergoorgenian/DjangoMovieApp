from rest_framework import serializers
from .models import MovieModel,CategoryModel,AuthorModel


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorModel
        fields ='__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
       model=CategoryModel
       fields='__all__'


class MovieSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=AuthorModel.objects.all())
    category = serializers.PrimaryKeyRelatedField(queryset=CategoryModel.objects.all())

    class Meta:
        model = MovieModel
        fields = ['name', 'description', 'author', 'category', 'release_date', 'rating', 'duration']

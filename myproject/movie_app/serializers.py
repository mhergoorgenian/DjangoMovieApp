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
    category = CategorySerializer()
    class Meta:
       model=MovieModel
       fields='__all__'

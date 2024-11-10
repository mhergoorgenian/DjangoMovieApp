from rest_framework import serializers
from .models import ProfileModel
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username','is_superuser']



class ProfileSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=ProfileModel
        fields = ['user','fullname']



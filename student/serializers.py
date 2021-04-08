from rest_framework import serializers
from .models import StudentData
from django.contrib.auth.models import User


class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model=StudentData
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import CustomUser

class userRegisterSerializer(RegisterSerializer):
    class Meta:
        model  = CustomUser
        fields = '__all__'
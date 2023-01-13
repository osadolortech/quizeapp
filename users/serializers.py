from rest_framework import serializers
from .models import Profile, User
from django.db import transaction
from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import UserDetailsSerializer




class Profile_serializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            "id","user","profile_pic","username","bio","created_at","updated_at"
        ]


class CustomRegistration(RegisterSerializer):
    name = serializers.CharField()
    
    @transaction.atomic
    def save(self, request):
        user = super().save(request)
        user.name = self.data.get('name')
        user.save()
        return user

class CustomUser(UserDetailsSerializer):
    class Meta:
        model = User
        fields = [
            "id", 'name','email','created_at','updated_at'
        ]
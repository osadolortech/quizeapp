from rest_framework import serializers
from .models import User,Profile




class Profile_serializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            "id","user","profile_pic","username","bio","created_at","updated_at"
        ]
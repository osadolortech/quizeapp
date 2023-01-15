from rest_framework.serializers import ModelSerializer
from .models import Quizes,Quesion


class QuizeSerializer(ModelSerializer):
    class Meta:
        model = Quizes
        fields = [
            'title'
        ]

class RandomQuestionSerializer(ModelSerializer):
    class Meta:
        model = Quesion
        fields = [
            'title','answer'
        ]
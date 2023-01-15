from rest_framework.serializers import ModelSerializer
from .models import Quizes,Quesion,Answers



class QuizeSerializer(ModelSerializer):
    class Meta:
        model = Quizes
        fields = [
            'title'
        ]

class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answers
        fields = [
            "id",
            "answer_text",
            "is_right"
        ]

class RandomQuestionSerializer(ModelSerializer):

    answer = AnswerSerializer(many=True,read_only=True)

    class Meta:
        model = Quesion
        fields = [
            'title','answer'
        ]
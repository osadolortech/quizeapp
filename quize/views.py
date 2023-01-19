from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from .models import Quizes,Quesion
from rest_framework.response import Response
from .serializers import QuizeSerializer,RandomQuestionSerializer,QuestionSerializer

# Create your views here.

class QuizeView(generics.ListAPIView):

    queryset = Quizes.objects.all()
    serializer_class = QuizeSerializer


class RandomView(APIView):

    def get(self,request,format=None, **kwargs):
        question = Quesion.objects.filter(quize__title=kwargs['topic']).order_by('?')[:1]
        serializer = RandomQuestionSerializer(question, many=True)
        return Response(serializer.data)

class QuestionQuize(APIView):

    def get(self,request,format=None, **kwargs):
        question = Quesion.objects.filter(quize__title=kwargs['topic'])
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)
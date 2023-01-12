from rest_framework.viewsets import ModelViewSet
from .models import Profile
from .serializers import Profile_serializer
from rest_framework.parsers import MultiPartParser,FormParser

# Create your views here.


class ProfileView(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = Profile_serializer
    parser_classes = [MultiPartParser,FormParser]
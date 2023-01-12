from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProfileView

router = DefaultRouter()
router.register('profile',ProfileView)

urlpatterns = [
    path('', include(router.urls))
]
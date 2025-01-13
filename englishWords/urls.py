from django.urls import path, include
from .views import CategoryViewSet, WordViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'words', WordViewSet, basename='word')

urlpatterns = [
    path('', include(router.urls)),
]

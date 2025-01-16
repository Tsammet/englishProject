from django.urls import path, include
from .views import CategoryViewSet, WordViewSet, GameScoreViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'words', WordViewSet, basename='word')
router.register(r'game_score', GameScoreViewSet, basename='game_score')  

urlpatterns = [
    path('', include(router.urls)),
]

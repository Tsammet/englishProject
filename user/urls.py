from django.urls import path
from .views import registerUser, loginUser, ProfileView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', registerUser.as_view(), name = 'register_user'),
    path('login', loginUser.as_view(), name = 'login_user'),
    path('profile', ProfileView.as_view(), name = 'profile')
] 

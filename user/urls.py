from django.urls import path
from .views import registerUser, loginUser

urlpatterns = [
    path('register', registerUser.as_view(), name = 'register_user'),
    path('login', loginUser.as_view(), name = 'login_user')
]

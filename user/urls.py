from django.urls import path
from .views import registerUser, loginUser
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register', registerUser.as_view(), name = 'register_user'),
    path('login', loginUser.as_view(), name = 'login_user')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
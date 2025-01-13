from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .serializer import RegisterSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Profile


class registerUser(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        serializer = RegisterSerializer(data = request.data)

        if serializer.is_valid():

            user = serializer.save()

            token = Token.objects.create(user = user)

            return Response({'token' : token.key, 'user': serializer.data}, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class loginUser(APIView):

    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):

        serializer = LoginSerializer(data = request.data)
        
        if serializer.is_valid():

            user = serializer.validated_data['user']

            token, created = Token.objects.get_or_create(user = user)

            profile = user.profile
            role = profile.role

            return Response({'token':token.key, 'username':user.username, 'role':role}, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    # Obtener el perfil del usuario autenticado
    def get(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile)
            return Response(serializer.data)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

    # Actualizar el perfil del usuario autenticado
    def put(self, request, *args, **kwargs):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer(profile, data=request.data, partial=True)  # 'partial=True' permite actualizar parcialmente el perfil
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Profile.DoesNotExist:
            return Response({"detail": "Profile not found."}, status=status.HTTP_404_NOT_FOUND)

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .serializer import RegisterSerializer, LoginSerializer

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
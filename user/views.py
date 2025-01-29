from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from .serializer import RegisterSerializer, LoginSerializer, GameScoreSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Profile
from englishWords.models import GameScore


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

            first_name = user.first_name
            last_name = user.last_name
            age = profile.age
            

            return Response({'token':token.key,
                             'user_id' : user.id,
                            'username':user.username, 
                            'role':role, 
                            'first_name' : first_name,
                            'last_name': last_name,
                            'age' : age}, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request):
        profile = request.user.profile

        game_scores = GameScore.objects.filter(user=request.user)

        game_scores_serializer = GameScoreSerializer(game_scores, many=True)

        return Response({
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'age': profile.age,
            'profile_picture': profile.profile_picture.url if profile.profile_picture else None,
            'game_scores': game_scores_serializer.data
        }, status=status.HTTP_200_OK)

    def put(self, request):
        profile = request.user.profile

        profile_picture = request.FILES.get('profile_picture')
        if profile_picture:
            profile.profile_picture = profile_picture

        age = request.data.get('age')
        if age:
            try:
                profile.age = int(age)
            except ValueError:
                return Response(
                    {"error": "Age must be a valid number."},
                    status=status.HTTP_400_BAD_REQUEST
                )

        profile.save()

        return Response({
            'message': 'Profile updated successfully',
            'profile_picture': profile.profile_picture.url if profile.profile_picture else None
        }, status=status.HTTP_200_OK)
from rest_framework import serializers
from .models import Profile
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from englishWords.models import GameScore

class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=Profile.USER_ROLE_CHOICES, default = 'user')
    age = serializers.IntegerField(required = True, write_only = True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'first_name', 'last_name', 'age']

    def create(self, validated_data):
        role = validated_data.pop('role', 'user')
        age = validated_data.pop('age')
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        Profile.objects.create(user = user, role = role, age = age)
        return user
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only = True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = authenticate(username = username, password = password)
        
        if user is None:
            raise serializers.ValidationError({
                "error" : "Credenciales incorrectas"
            })
        
        data['user'] = user

        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['age', 'profile_picture']



class GameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameScore
        fields = ['id', 'score', 'category', 'created_at']  # Incluye los campos que quieres mostrar

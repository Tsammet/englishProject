from rest_framework import serializers
from .models import Category, Words, GameScore

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id' ,'name' ,'description']

    def validate_name(self, value):
        if Category.objects.filter(name = value).exists():
            raise serializers.ValidationError('The category name already exists')
        return value
    
class WordSerializer(serializers.ModelSerializer):

    class Meta:
        model = Words
        fields = ['id', 'category', 'word', 'meaning']

    def validate_word(self, value):

        if self.instance:
            return value

        if Words.objects.filter(word = value).exists():
            raise serializers.ValidationError('The word already exists')
        return value
    

class GameScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameScore
        fields = ['user', 'score', 'category', 'created_at']
        read_only_fields = ['user', 'date']
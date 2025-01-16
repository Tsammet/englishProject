from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):

    name = models.CharField(max_length = 25)
    description = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    
class Words(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=False, null=False)
    word = models.CharField(max_length = 25, blank=False, null=False)
    meaning = models.CharField(max_length= 25, blank=False, null=False)
    
    def __str__(self):
        return self.word
    

class GameScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.category} - {self.score}'
from django.db import models

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
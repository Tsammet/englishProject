from rest_framework import viewsets
from .models import Category, Words
from .serializer import CategorySerializer, WordSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from random import sample
from rest_framework.decorators import action

class CategoryViewSet(viewsets.ViewSet):

    """
        El viewSet lo uso para manejar operaciones sobre la entidad Categoria
    """

    permission_classes = [IsAuthenticated]
    
    # aquí voy a crear una categoría

    def create(self, request):

        serializer = CategorySerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = 201)
    
        return Response(serializer.error, status = 400)
    
    # Listar todas las categorías 

    def list(self, request):

        querySet = Category.objects.all()
        serializer = CategorySerializer(querySet, many = True)
        return Response(serializer.data)
    
    # Buscar una categoría 

    def retrieve(self, request, pk=None):
        
        querySet = Category.objects.get(pk = pk)
        serializer = CategorySerializer(querySet)
        return Response(serializer.data)
    
    # Actualizar una categoría

    def update(self, request, pk = None):

        category = Category.objects.get(pk = pk)
        serializer = CategorySerializer(category, data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors, status = 400)
    
    # Eliminar una categoría 
    
    def delete(self, request, pk = None):
        
        category = Category.objects.get(pk = pk)
        category.delete()
        return Response(status=204)
    

class WordViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated]

    def create(self, request):

        serializer = WordSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=204)
        return Response(serializer.error, status=400)
    

    def list(self, request):

        querySet = Words.objects.all()
        serializer = WordSerializer(querySet, many = True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def get_random(self, request):
    
        count = int(request.GET.get('count', 2))
        category_name = request.GET.get('category', None)
        print(f"Count: {count}, Category: {category_name}")  # Debug


        if category_name:
            words = Words.objects.filter(category__name = category_name)
        else:
            words = Words.objects.all()

        random_Words = sample(list(words), min(count, len(words)))

        response_data = [
            {'word': word.word, 'meaning': word.meaning} for word in random_Words
        ]

        return Response(response_data)
    

    def retrieve(self, request, pk = None):

        querySet = Words.objects.get(pk = pk)
        serializer = WordSerializer(querySet)
        return Response(serializer.data)
    

    def update(self, request, pk = None):

        word = Words.objects.get(pk = pk)
        serializer = WordSerializer(word, data = request.data)
    
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status = 400)
    
    
    def delete(self, request, pk = None):

        word = Words.objects.get(pk = pk)
        word.delete()
        return Response('Word was deleted')
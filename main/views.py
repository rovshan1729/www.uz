from .serializers import ScoreBoardSerializer, CategorySerializer, RecentlyAddedSerializer
from .models import ScoreBoard, Category
from rest_framework import generics

class ScoreBoardListAPIView(generics.ListAPIView):
    queryset = ScoreBoard.objects.all(
    ).select_related('subcategory').order_by('-rating')
    serializer_class = ScoreBoardSerializer
    

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class RecentlyAddedAPIView(generics.ListAPIView):
    queryset = ScoreBoard.objects.all(
    ).select_related('subcategory').order_by('-created_at')
    serializer_class = RecentlyAddedSerializer


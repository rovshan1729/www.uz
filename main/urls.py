from django.urls import path
from .views import ScoreBoardListAPIView, CategoryListAPIView, RecentlyAddedAPIView

urlpatterns = [
    path("score-board/", ScoreBoardListAPIView.as_view()),
    path("category/", CategoryListAPIView.as_view()),
    path("recently-added/", RecentlyAddedAPIView.as_view()),
]

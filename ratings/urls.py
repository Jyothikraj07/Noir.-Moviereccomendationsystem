from django.urls import path
from .views import RatingView, RatingDeleteView, ratings_page

urlpatterns = [
    path("", RatingView.as_view()),
    path("<int:pk>/", RatingDeleteView.as_view()),
    path("ui/", ratings_page),
]
from django.urls import path
from .views import WatchlistView, WatchlistDeleteView, watchlist_page

urlpatterns = [
    path("", WatchlistView.as_view()),
    path("<int:pk>/", WatchlistDeleteView.as_view()),
    path("ui/", watchlist_page),
]
from django.urls import path

from .views import (
    MovieListCreateView,
    MovieDetailView,
    SearchMovieView,
    TrendingMoviesView,
    MovieFilterView
)
from .frontend_views import home, register_page, login_page


urlpatterns = [
    path("", MovieListCreateView.as_view()),

    path("<int:pk>/", MovieDetailView.as_view()),

    path(
        "search/",
        SearchMovieView.as_view()
    ),

    path(
        "trending/",
        TrendingMoviesView.as_view()
    ),
    path("ui/", home, name="home"),
    path("filter/", MovieFilterView.as_view())
    
]
from rest_framework import generics
from .models import Movie
from .serializers import MovieSerializer
from .pagination import MoviePagination



class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SearchMovieView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        query = self.request.GET.get("q", "")
        return Movie.objects.filter(
            title__icontains=query
        )
    
class TrendingMoviesView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        return Movie.objects.order_by(
            "-avg_rating"
        )[:20]
    
class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    pagination_class = MoviePagination

class MovieFilterView(generics.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):

        genre = self.request.GET.get("genre")
        language = self.request.GET.get("language")
        tier = self.request.GET.get("tier")

        queryset = Movie.objects.all()

        if genre:
            queryset = queryset.filter(genre__iexact=genre)

        if language:
            queryset = queryset.filter(language__iexact=language)

        if tier:
            queryset = queryset.filter(avg_rating__gte=tier)

        return queryset.order_by("-avg_rating")
from rest_framework import serializers
from .models import Watchlist
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class WatchlistSerializer(serializers.ModelSerializer):

    movie_details = MovieSerializer(
        source="movie",
        read_only=True
    )

    class Meta:
        model = Watchlist
        fields = "__all__"
        read_only_fields = ["user"]
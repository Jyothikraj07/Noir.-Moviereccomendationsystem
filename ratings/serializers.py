from rest_framework import serializers
from .models import Rating
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):

    movie_details = MovieSerializer(
        source="movie",
        read_only=True
    )

    class Meta:
        model = Rating
        fields = "__all__"
        read_only_fields = ["user"]
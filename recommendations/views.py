from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from movies.models import Movie
from ratings.models import Rating
from watchlist.models import Watchlist


class RecommendationView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        # STEP 1: Fetch user ratings
        ratings = Rating.objects.filter(user=user)

        # STEP 2: Cold start (new user)
        if not ratings.exists():

            watchlist = Watchlist.objects.filter(user=user)

            if watchlist.exists():

                genres = []

                for item in watchlist:
                    genres.append(item.movie.genre)

                movies = Movie.objects.filter(
                    genre__in=genres
                ).order_by('-avg_rating')[:10]

            else:

                movies = Movie.objects.order_by(
                    '-avg_rating'
                )[:10]

            return Response({
                "message": "New user recommendations",
                "recommendations": list(
                    movies.values(
                        'id',
                        'title',
                        'genre',
                        'language',
                        'avg_rating'
                    )
                )
            })

        # STEP 3: Find favourite genre
        genre_score = {}

        for rating in ratings:

            genre = rating.movie.genre

            genre_score[genre] = (
                genre_score.get(genre, 0)
                + rating.rating
            )

        favorite_genre = max(
            genre_score,
            key=genre_score.get
        )

        # STEP 4: Get watched movies
        watched_movies = ratings.values_list(
            'movie_id',
            flat=True
        )

        # STEP 5: Recommend unseen movies
        recommendations = Movie.objects.filter(
            genre=favorite_genre,
            avg_rating__gte=4
        ).exclude(
            id__in=watched_movies
        ).order_by(
            '-avg_rating'
        )[:10]

        return Response({

            "favorite_genre": favorite_genre,

            "recommendations": list(
                recommendations.values(
                    'id',
                    'title',
                    'genre',
                    'language',
                    'avg_rating'
                )
            )
        })
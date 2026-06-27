from django.core.management.base import BaseCommand
from movies.models import Movie
from movies.services.tmdb import fetch_popular_movies, GENRE_MAP


class Command(BaseCommand):
    help = "Import movies from TMDB API"

    def handle(self, *args, **kwargs):

        movies = fetch_popular_movies()

        if not movies:
            self.stdout.write(self.style.ERROR("No movies fetched from TMDB"))
            return

        count = 0

        for m in movies:

            tmdb_id = m.get("id")
            if not tmdb_id:
                continue

            # SAFE GENRE HANDLING
            genre_name = "Unknown"
            if m.get("genre_ids"):
                first_genre_id = m["genre_ids"][0]
                genre_name = GENRE_MAP.get(first_genre_id, "Unknown")

            release_year = 0
            if m.get("release_date"):
                try:
                    release_year = int(m["release_date"][:4])
                except:
                    release_year = 0

            obj, created = Movie.objects.update_or_create(
                tmdb_id=tmdb_id,   # 🔥 FIX IS HERE
                defaults={
                    "title": m.get("title", "No Title"),
                    "genre": genre_name,
                    "language": m.get("original_language", "en"),
                    "release_year": release_year,
                    "description": m.get("overview", ""),
                    "avg_rating": m.get("vote_average", 0),
                    "poster": (
                        f"https://image.tmdb.org/t/p/w500{m['poster_path']}"
                        if m.get("poster_path")
                        else ""
                    )
                }
            )

            if created:
                count += 1

        self.stdout.write(
            self.style.SUCCESS(f"{count} movies imported successfully")
        )
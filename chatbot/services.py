from google import genai
from django.conf import settings
from movies.models import Movie

client = genai.Client(api_key=settings.GEMINI_API_KEY)


def ask_movie_bot(user_query):

    movies = Movie.objects.all()[:20]

    if not movies.exists():

        return {
            "text": "No movies available in the database.",
            "movies": []
        }

    movie_context = "\n\n--- MOVIE ---\n\n".join(
        f"""
Title: {movie.title}
Genre: {movie.genre}
Language: {movie.language}
Year: {movie.release_year}
Description: {movie.description}
"""
        for movie in movies
    )

    prompt = f"""
You are NOIR, an AI movie recommendation assistant.

Use ONLY the movies given below.

{movie_context}

User Question:
{user_query}

Rules:
- Prefer movies from the database.
- Mention the exact movie titles from the database.
- Explain why you recommend each movie.
- Return recommendations as a numbered list.
- If nothing matches, politely say so.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )

        recommended_movies = []

        response_text = response.text

        for movie in movies:

            if movie.title.lower() in response_text.lower():

                recommended_movies.append({
                    "id": movie.id,
                    "title": movie.title
                })

        return {
            "text": response_text,
            "movies": recommended_movies
        }

    except Exception as e:

        return {
            "text": f"Error: {str(e)}",
            "movies": []
        }
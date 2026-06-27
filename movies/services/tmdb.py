import requests
import time
import os
from dotenv import load_dotenv

load_dotenv() 
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
print("TMDB API KEY:", TMDB_API_KEY) 
BASE_URL = "https://api.themoviedb.org/3"


def fetch_popular_movies(pages=50):

    all_movies = []

    for page in range(1, pages + 1):

        try:

            print(f"Fetching page {page}...")

            url = f"{BASE_URL}/movie/popular?api_key={TMDB_API_KEY}&page={page}"

            response = requests.get(url, timeout=30)

            data = response.json()

            all_movies.extend(data.get("results", []))

            time.sleep(1)   # Give VPN/TMDB some rest

        except Exception as e:

            print(f"Page {page} failed: {e}")

            continue

    return all_movies

GENRE_MAP = {
    28: "Action",
    12: "Adventure",
    16: "Animation",
    35: "Comedy",
    80: "Crime",
    18: "Drama",
    14: "Fantasy",
    27: "Horror",
    878: "Science Fiction",
    53: "Thriller",
    10749: "Romance",
}
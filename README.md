# 🎬 NOIR - Movie Recommendation System

NOIR is a full-stack movie recommendation web application built with Django and Django REST Framework. Users can register, browse movies, rate films, manage their watchlist, and receive personalized recommendations based on their preferences.

## 🚀 Features

### 🔐 Authentication
- User Registration
- JWT Authentication
- Secure API endpoints
- Login and Logout functionality

### 🎥 Movie Management
- Browse movies with pagination
- View movie details
- Search and filter movies
- TMDB movie import support
- Movie posters and descriptions

### ⭐ Rating System
- Rate movies (1–5 stars)
- Update existing ratings
- Automatic average rating calculation

### ❤️ Watchlist
- Add movies to watchlist
- Remove movies from watchlist
- View saved movies

### 🤖 Recommendation Engine
- Personalized recommendations based on user ratings
- Cold-start handling for new users
- Genre-based recommendation logic
- Top-rated movie suggestions

---

## 🛠️ Tech Stack

### Backend
- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### External APIs
- TMDB API (for importing movie data)

---

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── config/              # Django project settings
├── movies/              # Movie management app
├── ratings/             # Movie ratings app
├── recommendations/     # Recommendation engine
├── users/               # Authentication system
├── watchlist/           # User watchlist functionality
├── templates/           # Frontend templates
├── static/              # CSS and JavaScript files
├── manage.py
└── requirements.txt
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Jyothikraj/movie-recommendation-system.git
cd movie-recommendation-system
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Linux/Mac

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the server:

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key
TMDB_API_KEY=your_tmdb_api_key
DEBUG=True
```

---

## 🎥 Import Movies from TMDB

The project includes a custom Django management command to import movies from TMDB.

Run:

```bash
python manage.py import_tmdb_movies
```

The script fetches movie details such as:

- Title
- Genre
- Language
- Release Year
- Description
- Poster URL
- TMDB ID

---

## 📡 API Endpoints

### Authentication

```text
POST /api/users/register/
POST /api/token/
POST /api/token/refresh/
```

### Movies

```text
GET /api/movies/
GET /api/movies/<id>/
```

### Ratings

```text
POST /api/ratings/
GET /api/ratings/
```

### Watchlist

```text
GET /api/watchlist/
POST /api/watchlist/
DELETE /api/watchlist/<movie_id>/
```

### Recommendations

```text
GET /api/recommendations/
```

---

## 🧠 Recommendation Logic

The recommendation system follows a simple content-based approach:

### Existing Users
- Collect user ratings
- Determine the user's favorite genre
- Exclude already watched movies
- Recommend highly-rated movies from the preferred genre

### New Users (Cold Start)
- If a watchlist exists:
  - Recommend movies from watchlist genres
- Otherwise:
  - Recommend globally top-rated movies

---

## 📸 Screenshots

Add screenshots here after deployment:

```text
screenshots/
├── home.png
├── recommendations.png
├── watchlist.png
└── login.png
```

---

## 🌐 Live Demo

Render Deployment:

```text
https://your-app-url.onrender.com
```

---

## 👨‍💻 Author

**Srinivasan Jyothik Raj**

GitHub:

https://github.com/Jyothikraj

---

## ⭐ Future Improvements

- Advanced recommendation algorithms
- Collaborative filtering
- Search functionality
- Genre filtering
- User profiles
- Movie reviews and comments
- Infinite scrolling
- Docker deployment

---

## 📜 License

This project is developed for educational and portfolio purposes.

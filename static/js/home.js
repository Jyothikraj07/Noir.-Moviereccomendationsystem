let currentPage = 1;

const token = localStorage.getItem("access");

if (!token) {
    window.location.href = "/users/login/ui/";
}

let movieContainer = document.getElementById("movieContainer");
let recommendBtn = document.getElementById("recommendBtn");


// Load Movies

window.onload = function () {
    loadMovies(currentPage);
};


async function loadMovies(page) {

    try {

        const response = await fetch(`/movies/?page=${page}`);

        const data = await response.json();

        displayMovies(data.results);

        // Show pagination
        document.querySelector(".pagination").style.display = "flex";

        document.getElementById(
            "pageNumber"
        ).innerText = `Page ${page}`;

        document.getElementById(
            "prevBtn"
        ).disabled = !data.previous;

        document.getElementById(
            "nextBtn"
        ).disabled = !data.next;

    }

    catch (error) {

        console.log(error);

    }

}


// Pagination

document.getElementById("nextBtn")
    .addEventListener("click", function () {

        currentPage++;

        loadMovies(currentPage);

});


document.getElementById("prevBtn")
    .addEventListener("click", function () {

        if (currentPage > 1) {

            currentPage--;

            loadMovies(currentPage);

        }

});


// Generate Recommendations

recommendBtn.addEventListener("click", function () {

    let genre = document.getElementById("genre").value;
    let language = document.getElementById("language").value;
    let tier = document.getElementById("tier").value;

    fetch(
        `/movies/filter/?genre=${genre}&language=${language}&tier=${tier}`
    )

        .then(response => response.json())

        .then(data => {

            let movies = data.results || data;

            displayMovies(movies);

            // Hide pagination for filtered movies
            document.querySelector(".pagination").style.display = "none";

        })

        .catch(error => console.log(error));

});


// Display Movies

function displayMovies(movies) {

    movieContainer.innerHTML = "";

    if (!movies || movies.length === 0) {

        movieContainer.innerHTML =
            "<h2>No movies found</h2>";

        return;

    }

    movies.forEach(movie => {

        movieContainer.innerHTML += `

        <div class="card">

            <img src="${movie.poster}"
                 alt="${movie.title}">

            <div class="details">

                <h3>${movie.title}</h3>

                <p>Genre: ${movie.genre}</p>

                <p>Language: ${movie.language}</p>

                <p>⭐ ${movie.avg_rating}</p>

                <button
                    class="watchlistBtn"
                    onclick="addToWatchlist(${movie.id})">

                    Add to Watchlist

                </button>

                <br><br>

                <select
                    onchange="rateMovie(${movie.id}, this.value)">

                    <option value="">
                        Rate Movie
                    </option>

                    <option value="1">1 ⭐</option>
                    <option value="2">2 ⭐</option>
                    <option value="3">3 ⭐</option>
                    <option value="4">4 ⭐</option>
                    <option value="5">5 ⭐</option>

                </select>

            </div>

        </div>

        `;

    });

}


// Refresh Access Token

async function refreshAccessToken() {

    const response = await fetch("/users/refresh/", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            refresh: localStorage.getItem("refresh")
        })

    });

    if (!response.ok) {

        localStorage.clear();

        alert(
            "Session expired. Please login again."
        );

        window.location.href =
            "/users/login/ui/";

        return null;

    }

    const data = await response.json();

    localStorage.setItem(
        "access",
        data.access
    );

    return data.access;

}


// Authenticated Fetch

async function authenticatedFetch(
    url,
    options = {}
) {

    options.headers = {

        ...options.headers,

        Authorization:
            "Bearer " +
            localStorage.getItem("access")

    };

    let response = await fetch(
        url,
        options
    );

    if (response.status === 401) {

        const newAccess =
            await refreshAccessToken();

        if (!newAccess) {

            return response;

        }

        options.headers.Authorization =
            "Bearer " + newAccess;

        response = await fetch(
            url,
            options
        );

    }

    return response;

}


// Add To Watchlist

async function addToWatchlist(movieId) {

    try {

        const response =
            await authenticatedFetch(
                "/watchlist/",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({
                        movie: movieId
                    })

                }
            );

        const data =
            await response.json();

        if (!response.ok) {

            throw new Error(
                data.error ||
                "Failed to add movie"
            );

        }

        alert(
            "Movie added to watchlist"
        );

    }

    catch (error) {

        console.log(error);

        alert(error.message);

    }

}


// Rate Movie

async function rateMovie(
    movieId,
    rating
) {

    if (rating === "") {

        return;

    }

    try {

        const response =
            await authenticatedFetch(
                "/ratings/",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        movie: movieId,

                        rating: rating

                    })

                }
            );

        const data =
            await response.json();

        if (!response.ok) {

            throw new Error(
                data.error ||
                "Failed to submit rating"
            );

        }

        alert(
            "Rating submitted"
        );

    }

    catch (error) {

        console.log(error);

        alert(error.message);

    }

}


// Logout

function logoutUser() {

    localStorage.removeItem(
        "access"
    );

    localStorage.removeItem(
        "refresh"
    );

    window.location.href =
        "/users/login/ui/";

}
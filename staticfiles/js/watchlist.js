const token = localStorage.getItem("access");

if (!token) {
    window.location.href = "/login/";
}

const watchlistContainer = document.getElementById("watchlistContainer");

fetch("/watchlist/", {

    headers: {
        "Authorization": "Bearer " + localStorage.getItem("access")
    }

})

.then(response => response.json())

.then(data => {

    console.log(data);

    displayWatchlist(data);

})

.catch(error => console.log(error));


function displayWatchlist(watchlist) {

    watchlistContainer.innerHTML = "";

    if (watchlist.length === 0) {

        watchlistContainer.innerHTML = "<h2>No movies in watchlist</h2>";

        return;

    }

    watchlist.forEach(item => {

        let movie = item.movie_details;

        watchlistContainer.innerHTML += `

        <div class="card">

            <img src="${movie.poster}" alt="${movie.title}">

            <div class="details">

                <h3>${movie.title}</h3>

                <p>${movie.genre}</p>

                <p>${movie.language}</p>

                <button
                    class="remove-btn"
                    onclick="removeMovie(${item.id})">

                    Remove

                </button>

            </div>

        </div>

        `;
    });

}


function removeMovie(id) {

    fetch(`/watchlist/${id}/`, {

        method: "DELETE",

        headers: {
            "Authorization": "Bearer " + localStorage.getItem("access")
        }

    })

    .then(response => {

        if (!response.ok) {

            throw new Error("Failed to remove movie");

        }

        alert("Movie removed");

        location.reload();

    })

    .catch(error => {

        console.log(error);

        alert(error.message);

    });

}
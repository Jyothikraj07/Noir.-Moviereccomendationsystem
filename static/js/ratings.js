const token = localStorage.getItem("access");

if (!token) {
    window.location.href = "/login/";
}

const ratingsContainer = document.getElementById("ratingsContainer");

fetch("/ratings/", {

    headers: {
        "Authorization": "Bearer " + localStorage.getItem("access")
    }

})

.then(response => response.json())

.then(data => {

    console.log(data);

    displayRatings(data);

})

.catch(error => console.log(error));


function displayRatings(ratings) {

    ratingsContainer.innerHTML = "";

    if (ratings.length === 0) {

        ratingsContainer.innerHTML = "<h2>No ratings found</h2>";

        return;

    }

    ratings.forEach(item => {

        let movie = item.movie_details;

        ratingsContainer.innerHTML += `

        <div class="card">

            <img src="${movie.poster}" alt="${movie.title}">

            <div class="details">

                <h3>${movie.title}</h3>

                <p>⭐ Your Rating: ${item.rating}</p>

                <p>${item.review || "No review"}</p>

            </div>

        </div>

        `;

    });

}
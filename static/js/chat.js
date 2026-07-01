const sendBtn = document.getElementById("send-btn");
const input = document.getElementById("message-input");
const chatBox = document.getElementById("chat-box");


sendBtn.addEventListener("click", sendMessage);


input.addEventListener("keypress", function (e) {

    if (e.key === "Enter") {
        sendMessage();
    }

});


// Send Message

async function sendMessage() {

    const message = input.value.trim();

    if (!message) return;

    chatBox.innerHTML += `
        <div class="user-message">
            ${message}
        </div>
    `;

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;

    try {

        const response = await fetch("/chat/", {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                message: message
            })

        });

        if (!response.ok) {
            throw new Error("Failed to get response");
        }

        const data = await response.json();

        let buttons = "";

        if (data.movies && data.movies.length > 0) {

            data.movies.forEach(movie => {

                buttons += `
                    <button
                        class="watchlist-ai-btn"
                        onclick="addToWatchlist(${movie.id})">

                        + Add ${movie.title}

                    </button>
                `;

            });

        }

        chatBox.innerHTML += `
            <div class="bot-message">

                ${data.response}

                <br><br>

                ${buttons}

            </div>
        `;

        chatBox.scrollTop = chatBox.scrollHeight;

    }

    catch (error) {

        console.error(error);

        chatBox.innerHTML += `
            <div class="bot-message">
                Something went wrong. Please try again.
            </div>
        `;

    }

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

        alert("Session expired. Please login again.");

        window.location.href = "/users/login/ui/";

        return null;

    }

    const data = await response.json();

    localStorage.setItem("access", data.access);

    return data.access;

}


// Authenticated Fetch

async function authenticatedFetch(url, options = {}) {

    options.headers = {
        ...options.headers,
        Authorization:
            "Bearer " +
            localStorage.getItem("access")
    };

    let response = await fetch(url, options);

    if (response.status === 401) {

        const newAccess =
            await refreshAccessToken();

        if (!newAccess) {
            return response;
        }

        options.headers.Authorization =
            "Bearer " + newAccess;

        response = await fetch(url, options);

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
                data.detail ||
                "Failed to add movie"
            );

        }

        alert("Movie added to watchlist!");

    }

    catch (error) {

        console.log(error);

        alert(error.message);

    }

}
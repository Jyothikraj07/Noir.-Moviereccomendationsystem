let loginBtn = document.getElementById("loginBtn");

loginBtn.addEventListener("click", loginUser);

function loginUser() {

    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let message = document.getElementById("message");

    fetch("/users/login/", {
        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            username: username,
            password: password
        })
    })

    .then(response => {

        if (!response.ok) {
            throw new Error("Invalid username or password");
        }

        return response.json();

    })

    .then(data => {

        console.log(data);

        // Save tokens
        localStorage.setItem("access", data.access);
        localStorage.setItem("refresh", data.refresh);

        message.innerHTML = "Login successful";

        // Redirect to home page after login
        window.location.href = "/movies/ui/";

    })

    .catch(error => {

        console.log(error);

        message.innerHTML = error.message;

    });

}
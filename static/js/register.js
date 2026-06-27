let registerBtn = document.getElementById("registerBtn");

registerBtn.addEventListener("click", registerUser);

function registerUser() {

    let username = document.getElementById("username").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    fetch("/users/register/", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({
            username: username,
            email: email,
            password: password
        })

    })

    .then(response => response.json())

    .then(data => {

        console.log(data);

        document.getElementById("message").innerHTML =
            "Registration Successful";

    })

    .catch(error => {

        console.log(error);

    });

}
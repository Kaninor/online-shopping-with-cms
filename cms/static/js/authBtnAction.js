function redirectToAuth(path) {
    location.href = path;
}

$("#login-btn-action").on("click", function() {
    redirectToAuth("/cms/login/");
});

$("#sign-up-btn-action").on("click", function() {
    redirectToAuth("/cms/signup/");
});
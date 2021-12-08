function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

$(".h3").on("click", function() {
    let num = $(".h3").text()[4] + $(".h3").text()[5];
    location.href = "/home/" + num;
});
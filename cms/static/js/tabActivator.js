switch (location.href) {
    case "http://127.0.0.1:8000/cms/":
        $("#dashboard").addClass("active");
        break;
    case "http://127.0.0.1:8000/cms/charts/":
        $("#statistics").addClass("active");
        break;
}

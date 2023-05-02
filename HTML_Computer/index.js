function ProcessExpand(event) {
    if(event.target.getAttribute("open") == "false") {
        event.target.innerHTML += "<br><br>";
        event.target.innerHTML += "<h3>".concat(event.target.getAttribute("expand")).concat("</h3>");
        event.target.setAttribute("open", "true");
    } else if(event.target.getAttribute("open") == "true") {
        event.target.innerHTML = event.target.getAttribute("closed");
        event.target.setAttribute("open", "false");
    }
}

var elems = document.getElementsByClassName("fill");
for(var i = 0; i < elems.length; i++) {
    elems[i].innerHTML = elems[i].getAttribute("closed");
    elems[i].addEventListener("click", ProcessExpand);
}
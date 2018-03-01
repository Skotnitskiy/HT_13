window.onscroll = function() {scrlNav()};

var navbar = document.getElementById("navbar");
var sidebar = document.getElementsByClassName("sidenav");
var sticky = navbar.offsetTop;

function scrlNav() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
        sidebar[0].style.top = "50px";
    } else {
        navbar.classList.remove("sticky");
        sidebar[0].style.top = "136px"
    }
}
// don't work
var lnkContainer = document.getElementById("sidenav");


var links = lnkContainer.getElementsByClassName("lnk");


for (var i = 0; i < links.length; i++) {
  links[i].addEventListener("onclick", function() {
     var current = document.getElementsByClassName("active");
     current[0].className = current[0].className.replace(" active", "");
    this.classList.add("active");
  });
}
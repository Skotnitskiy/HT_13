window.onscroll = function() {scrlNav()};


var navbar = document.getElementById("navbar");
var sidebar = document.getElementsByClassName("sidenav");


var sticky = navbar.offsetTop;
var sideSticky = sidebar.offsetTop;

function scrlNav() {
    if (window.pageYOffset >= sticky) {
        navbar.classList.add("sticky");
        sidebar[0].style.top = "50px";
    } else {
        navbar.classList.remove("sticky");
        sidebar[0].style.top = "136px"
    }
}
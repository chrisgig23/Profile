window.onscroll = function() {lockHeader()};

var header = document.getElementById('header');

var sticky = header.offsetTop;

function lockHeader() {
  if (window.pageYOffset > sticky) {
    header.classList.add("sticky");
  } else {
    header.classList.remove("sticky");
  }
}


function showHideMenu() {
  var x = document.getElementById("topNav");
  if (x.className === "nav-bar") {
    x.className += " responsive";
  } else {
    x.className = "nav-bar";
  }
}

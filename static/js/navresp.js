
function myFunction() {
  var x = document.getElementById("navid");
  if (x.className === "nav-bar") {
    x.className += " responsive";
  } else {
    x.className = "nav-bar";
  }
}
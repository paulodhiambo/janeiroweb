var scrolls = document.getElementById("scrolls");

function scrollRight() {
  scrolls.scrollBy(470, 0);
}

function scrollLft() {
  scrolls.scrollBy(-470, 0);
}

var menu = document.getElementById("menu");

function openMenu() {
  menu.style.right = "0";
}

function closeMenu() {
  menu.style.right = "-100vw";
}
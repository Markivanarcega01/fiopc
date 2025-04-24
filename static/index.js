function toggleMenu(x) {
  x.classList.toggle("change");
  document.querySelector('.nav-links-mobile').classList.toggle('show');
}

function toggleMenu(element) {
  element.classList.toggle("active");

  const nav = document.querySelector('.nav-links-mobile');
  nav.classList.toggle("show");
}
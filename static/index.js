// navigation bar burger menu
function toggleMenu(x) {
  x.classList.toggle("change");
  document.querySelector('.nav-links-mobile').classList.toggle('show');
}

// navigation bar links
function toggleMenu(element) {
  element.classList.toggle("active");

  const nav = document.querySelector('.nav-links-mobile');
  nav.classList.toggle("show");
}

// navigation bar links
function toggleCollapse(element) {
  element.parentElement.classList.toggle('active');
}

// careers page modal
// function openModal() {
//   document.getElementById("modalOverlay").style.display = "flex";
// }

// // careers page modal close button
// function closeModal() {
//   document.getElementById("modalOverlay").style.display = "none";
// }

// careers success message close button
function closeCareersSuccessModal() {
  document.getElementById('careersSuccessModal').style.display = 'none';
}

// careers page modal form submission
function openCareersModal(jobId) {
  document.getElementById("careersModalOverlay").style.display = "flex";
  document.getElementById("job_id_input").value = jobId;
}
function closeCareersModal() {
  document.getElementById("careersModalOverlay").style.display = "none";
}

// Contacts page
function closeContactsSuccessModal() {
  document.getElementById("contactsSuccessModal").style.display = "none";
}

// Home page carousel
const slides = document.querySelectorAll('.carousel-item');
const dots = document.querySelectorAll('.dot');
let currentIndex = 0;
function updateCarousel(index) {
  const carouselInner = document.querySelector('.carousel-inner');
  carouselInner.style.transform = `translateX(-${index * 100}%)`;
  dots.forEach(dot => dot.classList.remove('active'));
  dots[index].classList.add('active');
}
document.querySelector('.next').addEventListener('click', () => {
  currentIndex = (currentIndex + 1) % slides.length;
  updateCarousel(currentIndex);
});
document.querySelector('.prev').addEventListener('click', () => {
  currentIndex = (currentIndex - 1 + slides.length) % slides.length;
  updateCarousel(currentIndex);
});
dots.forEach((dot, index) => {
  dot.addEventListener('click', () => {
    currentIndex = index;
    updateCarousel(index);
  });
});

// Home page collapsible text
const text = document.getElementById("text");
    const toggleBtn = document.getElementById("toggleBtn");
    toggleBtn.addEventListener("click", () => {
      text.classList.toggle("expanded");
      toggleBtn.textContent = text.classList.contains("expanded") ? "See Less" : "See More";
    });
    
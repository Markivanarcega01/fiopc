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

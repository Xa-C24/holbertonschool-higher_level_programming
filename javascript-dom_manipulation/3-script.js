const toggleHeader = document.getElementById('toggle_header');
// Sélectionne l'élément <header>
const header = document.querySelector('header');

// Ajoute un gestionnaire d'événement pour le clic
toggleHeader.addEventListener('click', function () {

  // Vérifie si <header> a la classe "red"
  if (header.classList.contains('red')) {
    // Si oui, remplace "red" par "green"
    header.classList.replace('red', 'green');
  } else {
    // Sinon, remplace "green" par "red"
    header.classList.replace('green', 'red');
  }
});

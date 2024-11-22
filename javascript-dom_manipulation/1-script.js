// Sélectionne l'élément <div> avec l'ID red_header
const redHeader = document.getElementById('red_header');

// Sélectionne l'élément <header>
const header = document.querySelector('header');

// Ajoute un gestionnaire d'événement pour le clic
redHeader.addEventListener('click', function() {
  // Change la couleur du texte de <header> en rouge
  header.style.color = '#FF0000';
});

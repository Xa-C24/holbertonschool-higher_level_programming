// Sélectionne l'élément avec l'ID update_header
const updateHeaderButton = document.getElementById('update_header');

// Sélectionne l'élément <header>
const header = document.querySelector('header');

// Ajoute un gestionnaire d'événement pour le clic
updateHeaderButton.addEventListener('click', function () {
  // Met à jour le texte de l'élément <header>
  header.textContent = 'New Header!!!';
});

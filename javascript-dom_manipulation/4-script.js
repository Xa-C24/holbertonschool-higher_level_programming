// Sélectionne l'élément avec l'ID add_item
const addItemButton = document.getElementById('add_item');

// Sélectionne la liste <ul> avec la classe my_list
const myList = document.querySelector('.my_list');

// Ajoute un gestionnaire d'événement pour le clic
addItemButton.addEventListener('click', function () {
  // Crée un nouvel élément <li>
  const newItem = document.createElement('li');

  // Ajoute du texte à cet élément
  newItem.textContent = 'Item';

  // Ajoute le nouvel élément <li> à la liste <ul>
  myList.appendChild(newItem);
});

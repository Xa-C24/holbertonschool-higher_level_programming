const apiUrl = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

// Sélectionne l'élément HTML où afficher le nom du personnage
const characterDiv = document.getElementById('character');

// Utiliser Fetch API pour récuperer des données
fetch(apiUrl)
  .then((response) => {

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    // Convertit la reponse en json
    return response.json();
  })
  .then((data) => {
    // Récupère le nom du personnage
    characterDiv.textContent = data.name;
  });

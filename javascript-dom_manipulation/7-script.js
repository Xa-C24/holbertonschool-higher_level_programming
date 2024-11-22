const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

// Sélectionne l'élément <ul> avec l'ID list_movies
const moviesList = document.getElementById('list_movies');

fetch(apiUrl)
  .then((response) => {
    // Vérifie si la réponse est OK
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    // Convertit la reponse en json
    return response.json();
  })
  .then((data) => {

    data.results.forEach((movie) => {
      // Crée un nouvel élément <li>
      const listItem = document.createElement('li');
      // Définit le texte de l'élément <li>
      listItem.textContent = movie.title;
      // ajouter l'élement <li> à la suite de <ul>
      moviesList.appendChild(listItem);
    });
  })
  .catch((error) => {
    // Gère les erreurs
    console.error('Erreur lors de la récupération des données :', error);
  });

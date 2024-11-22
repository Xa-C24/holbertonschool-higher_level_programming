document.addEventListener('DOMContentLoaded', () => {
  // URL de l'API
  const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

  // Sélectionne l'élément où afficher le texte
  const helloDiv = document.getElementById('hello');

  // Utilise Fetch API pour récupérer les données
  fetch(apiUrl)
    .then((response) => {
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return response.json();
    })
    .then((data) => {
      // Met à jour le contenu de l'élément avec la traduction
      helloDiv.textContent = data.hello;
    })
    .catch((error) => {
      console.error('Erreur lors de la récupération des données :', error);
      helloDiv.textContent = 'Une erreur est survenue';
    });
});

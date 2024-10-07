# RESTful API  


## 0. Basics of HTTP/HTTPS  

##1.Differentiating HTTP and HTTPS:##  


**HTTP (HyperText Transfer Protocol) :**   

**Protocole non sécurisé :**   
HTTP ne chiffre pas les données qui transitent entre le client (navigateur) et le serveur.  
Cela signifie que les informations envoyées via HTTP peuvent être facilement interceptées par des tiers (attaquants, pirates). 
Port 80 : Le protocole HTTP utilise par défaut le port 80 pour la communication entre le client et le serveur.  
Vulnérabilité : Les communications HTTP peuvent être vulnérables à des attaques comme le man-in-the-middle (interception des données en transit), car les données ne sont pas chiffrées.  

**HTTPS (HyperText Transfer Protocol Secure) :**  

Protocole sécurisé : HTTPS est la version sécurisée de HTTP. Il utilise des protocoles de chiffrement comme SSL (Secure Sockets Layer) ou TLS (Transport Layer Security) pour protéger les données en transit.  
Le cryptage rend les données illisibles pour quiconque intercepte la communication.  
Port 443 : HTTPS utilise le port 443 par défaut pour les communications sécurisées.  
Certificat SSL/TLS : HTTPS nécessite un certificat SSL/TLS qui authentifie le serveur et établit une connexion sécurisée. Le certificat est émis par une autorité de certification (CA).  
Confidentialité et intégrité des données : Grâce au chiffrement, même si les données sont interceptées, elles restent illisibles. De plus, HTTPS garantit l’intégrité des données, c'est-à-dire qu’elles ne peuvent pas être modifiées en transit sans être détectées.  

**HTTP** : Pas de chiffrement, les données sont transmises en clair.  
**HTTPS** : Chiffrement des données avec SSL/TLS, garantissant la confidentialité des échanges.  


 **Cas d’utilisation :**   

HTTP est généralement utilisé pour les sites ou services qui n’ont pas besoin de sécurité renforcée, comme des blogs ou des sites publics qui ne traitent pas de données sensibles.  
HTTPS est essentiel pour les sites qui gèrent des informations sensibles, comme les services bancaires en ligne, les boutiques e-commerce, les systèmes de gestion de comptes utilisateurs, etc.  




##3.Exploring HTTP Methods and Status Codes:##    

Ces éléments sont essentiels pour comprendre comment les clients (comme les navigateurs) et les serveurs web communiquent.  

**Méthodes HTTP courantes:**  
Les méthodes HTTP (ou verbes HTTP) définissent l’action que le client souhaite réaliser sur une ressource (comme une page web, un fichier ou des données).  
Voici une liste des méthodes les plus courantes, accompagnée de leur utilisation typique.  

**GET :**  
Description :  
La méthode GET est utilisée pour récupérer des données depuis un serveur. Elle est principalement utilisée pour charger des pages web ou pour demander des ressources spécifiques (comme des images, fichiers, etc.).  
Utilisation :  
Lorsque tu charges une page web dans ton navigateur, une requête GET est envoyée pour récupérer le contenu de la page.  

**POST :**  
Description :  
La méthode POST est utilisée pour envoyer des données au serveur. C’est souvent utilisé pour soumettre des formulaires, télécharger des fichiers, ou envoyer des données pour créer de nouvelles ressources sur le serveur.  
Utilisation :  
Lorsque tu soumets un formulaire de contact sur un site web ou que tu ajoutes un produit dans ton panier, une requête POST est utilisée pour transmettre ces informations au serveur.  

**PUT :**  
Description :  
La méthode PUT est utilisée pour mettre à jour ou remplacer une ressource existante sur le serveur.  
Contrairement à POST, qui est utilisé pour créer de nouvelles ressources, PUT remplace entièrement une ressource existante.  
Utilisation :  
Lorsque tu modifies ton profil utilisateur ou que tu mets à jour un article, une requête PUT est souvent envoyée pour remplacer les anciennes données par les nouvelles.  

**DELETE :**  
Description :  
La méthode DELETE est utilisée pour supprimer une ressource du serveur.  
Utilisation :  
Si tu veux supprimer un compte utilisateur ou un article de blog, une requête DELETE est envoyée au serveur pour indiquer qu'une ressource doit être supprimée.  
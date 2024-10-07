#RESTful API  


##0. Basics of HTTP/HTTPS
**1.Differentiating HTTP and HTTPS:**  

HTTP (HyperText Transfer Protocol) :  
Protocole non sécurisé : HTTP ne chiffre pas les données qui transitent entre le client (navigateur) et le serveur.  
Cela signifie que les informations envoyées via HTTP peuvent être facilement interceptées par des tiers (attaquants, pirates). 
Port 80 : Le protocole HTTP utilise par défaut le port 80 pour la communication entre le client et le serveur.  
Vulnérabilité : Les communications HTTP peuvent être vulnérables à des attaques comme le man-in-the-middle (interception des données en transit), car les données ne sont pas chiffrées.  

HTTPS (HyperText Transfer Protocol Secure) :

Protocole sécurisé : HTTPS est la version sécurisée de HTTP. Il utilise des protocoles de chiffrement comme SSL (Secure Sockets Layer) ou TLS (Transport Layer Security) pour protéger les données en transit.  
Le cryptage rend les données illisibles pour quiconque intercepte la communication.  
Port 443 : HTTPS utilise le port 443 par défaut pour les communications sécurisées.  
Certificat SSL/TLS : HTTPS nécessite un certificat SSL/TLS qui authentifie le serveur et établit une connexion sécurisée. Le certificat est émis par une autorité de certification (CA).  
Confidentialité et intégrité des données : Grâce au chiffrement, même si les données sont interceptées, elles restent illisibles. De plus, HTTPS garantit l’intégrité des données, c'est-à-dire qu’elles ne peuvent pas être modifiées en transit sans être détectées.  

HTTP : Pas de chiffrement, les données sont transmises en clair.  
HTTPS : Chiffrement des données avec SSL/TLS, garantissant la confidentialité des échanges.  


 Cas d’utilisation :  
HTTP est généralement utilisé pour les sites ou services qui n’ont pas besoin de sécurité renforcée, comme des blogs ou des sites publics qui ne traitent pas de données sensibles.  
HTTPS est essentiel pour les sites qui gèrent des informations sensibles, comme les services bancaires en ligne, les boutiques e-commerce, les systèmes de gestion de comptes utilisateurs, etc.  
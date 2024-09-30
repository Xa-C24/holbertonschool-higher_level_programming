**Python - Input/Output**  

In Python, the term Input/Output (I/O) refers to the mechanisms by which a program interacts with its environment,  
in particular to read data (input) and write data (output).  
Here's an overview of the concept:  

1. Input  
In Python, input is used to receive data from the user or from another source, such as a file or database.  

        nom = input("Entrez votre nom : ")
print("Bonjour", nom)

Lecture depuis un fichier : Utilisation de méthodes comme open() pour lire le contenu d’un fichier.  

    with open("mon_fichier.txt", "r") as fichier:
    contenu = fichier.read()
    print(contenu)
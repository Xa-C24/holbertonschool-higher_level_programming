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


2. Output  
The output is used to display information on the screen or to write it to a file.  
Here are some examples: - On-screen display: Use print() to display data in the console.  

        print("Ceci est un message à afficher.")  

Writing to a file: Use open() with write mode ("w", "a") to save data to a file.  

        with open("sortie.txt", "w") as fichier:
        fichier.write("Ceci est du texte écrit dans le fichier.")  


3. File management  
In Python, you can work with files by opening them using the open() function.  
This function takes two main arguments: the file name and the open mode.  
- r : Read-only (default mode)  
- w: Write (deletes the contents of the file if it exists)   
- a : Add content to the end of the file without deleting existing content   
- rb or wb: Read or write in binary mode (for working with non-text files such as images)  

        with open("mon_fichier.txt", "w") as fichier:
        fichier.write("Voici du texte à écrire dans le fichier.")  

4. Streams Python  
uses streams to manage I/O.  
There are three main streams that are automatically available in every Python program:  
- stdin: for standard input (for example, user input with input()).  
- stdout: for standard output (for example, display with print()).  
- stderr : for error message output.  

        # Demande d'input à l'utilisateur
        nom = input("Entrez votre nom : ")

        # Output à l'écran
        print(f"Bonjour, {nom} !")

        # Écriture dans un fichier
        with open("salutations.txt", "w") as fichier:
        fichier.write(f"Bonjour, {nom} !")  

In a nutshell, Input/Output in Python is anything that allows your program to read data from the outside  (such as a user or a file) and write data to the outside (such as displaying it on the screen or saving it to a file).  
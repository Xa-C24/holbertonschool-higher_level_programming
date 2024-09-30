**Python - Input/Outpu  Serialization/Deserialization**  

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

**Sérialisation/Deserialization**  

Serialization and deserialization are important concepts in programming, particularly for data management.

1. Serialization   
Serialization is the process of converting an object or data structure into a format that can be easily stored or transmitted.  
This format is often a text format (such as JSON, XML) or a binary format (such as BSON, pickle in Python).  
The idea is to take the data in memory (such as a list, a dictionary or an object) and convert it into a character string or a sequence of bytes.  

-Stored in a file or database,  
- Sent via a network to another programme or machine.  

2. Deserialization  
Deserialization is the reverse operation of serialization.   
It involves taking the serialized data (stored as a string or bytes) and converting it back to its original format, i.e. an object, a list, a dictionary, etc.  
In other words, it reconstructs the object or data structure from its serialised format.  

Common uses:  
- Save state: Serialise an object to save it (for example, in a file) so that it can be restored later (deserialise).  
- Data transmission: In network communications (for example, via APIs or sockets), serialization allows data to be transmitted from one program to another using a standard format such as JSON or XML.  
- Databases: Some databases can store serialized objects.  

In short:  

- Serialization: Conversion of an object into a storable or transmittable format (e.g. JSON, binary).  
- Deserialization: Reconstitution of the object from this serialized format. These processes are widely used in programming to facilitate the storage, transmission of data and persistence of objects between program executions.  
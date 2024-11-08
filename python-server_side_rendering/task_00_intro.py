import os

def generate_invitations(template, attendees):
    # Vérification du type d'entrée
    if not isinstance(template, str):
        print("Error: Template should be a string.")
        return
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print("Error: Attendees should be a list of dictionaries.")
        return
    
    # Vérification des entrées vides
    if not template:
        print("Template is empty, no output files generated.")
        return
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Génération des invitations pour chaque participant
    for i, attendee in enumerate(attendees, start=1):
        # Remplacer les espaces réservés dans le modèle
        output_text = template.format(
            name=attendee.get("name", "N/A"),
            event_title=attendee.get("event_title", "N/A"),
            event_date=attendee.get("event_date", "N/A"),
            event_location=attendee.get("event_location", "N/A")
        )

        # Écrire dans un fichier de sortie
        output_file = f"output_{i}.txt"
        with open(output_file, "w") as file:
            file.write(output_text)
        print(f"Generated {output_file}")
    
# Exemple d'utilisation
with open('template.txt', 'r') as file:
    template_content = file.read()

attendees = [
    {"name": "Alice", "event_title": "Python Conference", "event_date": "2023-07-15", "event_location": "New York"},
    {"name": "Bob", "event_title": "Data Science Workshop", "event_date": "2023-08-20", "event_location": "San Francisco"},
    {"name": "Charlie", "event_title": "AI Summit", "event_date": None, "event_location": "Boston"}
]

generate_invitations(template_content, attendees)

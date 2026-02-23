from datetime import datetime

def afficher_moment_present():
    # Récupérer la date et l'heure actuelles
    maintenant = datetime.now()

    # Formater l'affichage de manière lisible
    # %d : jour, %m : mois, %Y : année
    # %H : heure, %M : minute, %S : seconde
    date_formatee = maintenant.strftime("%A %d %B %Y")
    heure_formatee = maintenant.strftime("%H:%M:%S")

    print(f"Nous sommes le : {date_formatee}")
    print(f"Il est actuellement : {heure_formatee}")

def main():
    print("Hello from cours-github!")
    afficher_moment_present()


if __name__ == "__main__":
    main()
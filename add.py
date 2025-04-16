#coding:utf-8
import json


fichier_json = 'donnees.txt'


def charger_donnees():
    try:
        with open(fichier_json, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []  
    except json.JSONDecodeError:
        return []  e

# Fonction pour sauvegarder des données dans le fichier
def sauvegarder_donnees(donnees):
    with open(fichier_json, 'w') as f:
        json.dump(donnees, f, indent=4)

# Charger les données existantes
donnees = charger_donnees()

# Ajouter de nouvelles données
nouvelle_donnee = {
    "id": input("Shiramwo ikidandazwa id : "),
    "izina": input("Izina ry'ikidandanzwa : "),
    "igiciro": float(input("Shiramwo igiciro : ")),
    "igitigiri": int(input("Shiramwo Igitigiri : "))
}

donnees.append(nouvelle_donnee)

# Sauvegarder les données mises à jour
sauvegarder_donnees(donnees)

print("Les données ont été ajoutées avec succès.")

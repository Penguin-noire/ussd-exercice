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


def sauvegarder_donnees(donnees):
    with open(fichier_json, 'w') as f:
        json.dump(donnees, f, indent=4)


donnees = charger_donnees()

nouvelle_donnee = {
    "id": input("Shiramwo ikidandazwa id : "),
    "izina": input("Izina ry'ikidandanzwa : "),
    "igiciro": float(input("Shiramwo igiciro : ")),
    "igitigiri": int(input("Shiramwo Igitigiri : "))
}

donnees.append(nouvelle_donnee)


sauvegarder_donnees(donnees)

print("Les données ont été ajoutées avec succès.")

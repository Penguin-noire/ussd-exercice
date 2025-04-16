#coding:utf-8
from pathlib import Path
import json

def ajouter_donnees():
    chemin_fichier = Path('fichier')
    chemin_fichier.mkdir(exist_ok=True)

    nom_fichier = f'data.json'
    fichier_complet = chemin_fichier / nom_fichier

    if fichier_complet.exists():
        with open(fichier_complet, 'r') as fi:
            try:
                donnees_existantes = json.load(fi)
            except json.JSONDecodeError:
                donnees_existantes = []
    else:
        donnees_existantes = []

    nouvelle_donnee = {
        "id": input("Shiramwo ikidandazwa id : "),
        "izina": input("Izina ry'ikidandanzwa : "),
        "igiciro": float(input("Shiramwo igiciro : ")),
        "igitigiri": int(input("Shiramwo Igitigiri : "))
    }

    donnees_existantes.append(nouvelle_donnee)

   
    with open(fichier_complet, 'w') as fi:
        json.dump(donnees_existantes, fi, ensure_ascii=False, indent=4)
    
    print("Muhejeje Gushiramwo Ibidandazwa.")


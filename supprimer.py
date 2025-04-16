# coding:utf-8
from pathlib import Path
import json

def supprimer_donnees():
    chemin_fichier = Path('fichier')
    nom_fichier = f'data.json'
    fichier_complet = chemin_fichier / nom_fichier

   
    if fichier_complet.exists():
        with open(fichier_complet, 'r') as fi:
            donnees = json.load(fi)

        choixsup = input("Shiramwo id yogufuta : ")
        
        
        donnees_filtrees = [donnee for donnee in donnees if donnee['id'] != choixsup]

        with open(fichier_complet, 'w') as fi:
            json.dump(donnees_filtrees, fi, ensure_ascii=False, indent=4)

        print("Ikidandazwa cafuswe neza.")
    else:
        print("Nta bibandazwa biriyo.")

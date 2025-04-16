# coding:utf-8
from pathlib import Path
import json

def modifier_donnees():
    chemin_fichier = Path('fichier')
    nom_fichier = f'data.json'
    fichier_complet = chemin_fichier / nom_fichier

    if fichier_complet.exists():
        with open(fichier_complet, 'r') as fi:
            donnees = json.load(fi)

        choixid = input("Shiramwo id yo guhindura : ")

        
        for donnee in donnees:
            if str(donnee['id']) == choixid:
               
                donnee['izina'] = input("Izina ry'ikidandanzwa risha: ")
                donnee['igiciro'] = float(input("Igiciro gishasha : "))
                donnee['igitigiri'] = int(input("Igitigiri gishasha : "))
                break
        else:
            print("ID ntibashije kuboneka.")
            return

        with open(fichier_complet, 'w') as fi:
            json.dump(donnees, fi, ensure_ascii=False, indent=4)

        print("Ibidandazwa vyahinduwe neza.")
    else:
        print("Nta bibandazwa biriyo.")

#coding:utf-8
from pathlib import Path
import json

def afficher_donnees():
    chemin_fichier = Path('fichier')
    nom_fichier = 'data.json'
    fichier_complet = chemin_fichier / nom_fichier

   
    if fichier_complet.exists():
        with open(fichier_complet, 'r') as fi:
            donnees = json.load(fi)
            for donnee in donnees:
                print(f"ID: {donnee['id']},\nIzina: {donnee['izina']},\nIgiciro: {donnee['igiciro']},\nIgitigiri: {donnee['igitigiri']}\n"+'*'*20)
    else:
        print("Nta bidandazwa biriyo.")


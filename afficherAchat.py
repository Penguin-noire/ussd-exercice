# coding:utf-8
from pathlib import Path
import json

def afficher_produits_vendus():
    chemin_fichier_achats = Path('fichier')
    nom_fichier_achats = 'achats.json'
    fichier_achats = chemin_fichier_achats / nom_fichier_achats

 
    if not fichier_achats.exists():
        print("Nta madosiye y'ibicuruzwa byaguzwe.")
        return

    # Lire les achats existants
    with open(fichier_achats, 'r', encoding='utf-8') as fi:
        achats = json.load(fi)

    total = 0

    if achats:
        print("Ibidandazwa vyaguzwe :")
        for achat in achats:
            date_achat = achat['date_achat'][:16]  # Format de date simplifié
            print(f"{date_achat} {achat['izina']} x {achat['igitigiri']} : {achat['igiciro_total']:,}")
            total += achat['igiciro_total']

        print(f"{' ' * 15} vyose hamwe : {total:,}")
    else:
        print("Nta bicuruzwa byaguzwe.")


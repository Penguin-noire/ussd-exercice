# coding:utf-8
from pathlib import Path
import json

def generer_rapport():
    chemin_fichier_achats = Path('fichier')
    nom_fichier_achats = 'achats.json'
    fichier_achats = chemin_fichier_achats / nom_fichier_achats

    
    if not fichier_achats.exists():
        print("Nta madosiye y'ibicuruzwa byaguzwe.")
        return

   
    with open(fichier_achats, 'r', encoding='utf-8') as fi:
        achats = json.load(fi)

    rapport = []
    total_achats = len(achats)
    montant_total = 0
    total_produits = 0

    
    if achats:
        rapport.append("Rapport y'ibicuruzwa byaguzwe :\n")
        for achat in achats:
            date_achat = achat['date_achat'][:16] 
            rapport.append(f"{date_achat} {achat['izina']} x {achat['igitigiri']} : {achat['igiciro_total']:,}")
            montant_total += achat['igiciro_total']
            total_produits += achat['igitigiri']

        rapport.append(f"\nMumaze kudandaza incuro : {total_achats}")
        rapport.append(f"Mumaze kudandaza amahera : {montant_total:,}")
        rapport.append(f"Ibidandazwa vyaheze : {total_produits}")
        rapport.append(f"Ibidandazwa vyose hamwe : {total_produits}")

        
        chemin_rapport = Path('fichier')
        nom_fichier_rapport = 'rapport.txt'
        fichier_rapport = chemin_rapport / nom_fichier_rapport

        with open(fichier_rapport, 'w', encoding='utf-8') as fr:
            fr.write("\n".join(rapport))

        print(f"Rapport yanditswe mu madosiye: {fichier_rapport}")
    else:
        print("Nta bicuruzwa byaguzwe.")

generer_rapport()

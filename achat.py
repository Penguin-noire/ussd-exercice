# coding:utf-8
from pathlib import Path
import json
from datetime import datetime

def acheter_produit():
    chemin_fichier_produits = Path('fichier')
    nom_fichier_produits = 'data.json'
    fichier_produits = chemin_fichier_produits / nom_fichier_produits

    chemin_fichier_achats = Path('fichier')
    nom_fichier_achats = 'achats.json'
    fichier_achats = chemin_fichier_achats / nom_fichier_achats

   
    if not fichier_produits.exists():
        print("Nta bibandazwa biriyo.")
        return

    
    with open(fichier_produits, 'r', encoding='utf-8') as fi:
        produits = json.load(fi)

    choixid = input("Entrez l'id du produit à acheter : ")
    igitiri = int(input("Entrez la quantité à acheter : "))

  
    produit_a_acheter = next((p for p in produits if str(p['id']) == choixid), None)

    if produit_a_acheter is None:
        print("ID ntibashije kuboneka.")
        return

  
    igiciro_total = produit_a_acheter['igiciro'] * igitiri

    
    achat = {
        "id": choixid,
        "izina": produit_a_acheter['izina'],
        "igiciro_unitaire": produit_a_acheter['igiciro'],
        "igitigiri": igitiri,
        "igiciro_total": igiciro_total,
        "date_achat": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if fichier_achats.exists():
        with open(fichier_achats, 'r') as fi:
            achats_existants = json.load(fi)
    else:
        achats_existants = []

  
    achats_existants.append(achat)

    
    with open(fichier_achats, 'w') as fi:
        json.dump(achats_existants, fi, ensure_ascii=False, indent=4)

    print("Igicuruzwa cyaguze neza.")


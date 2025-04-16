#coding:utf-8
import re
import afficher
import ajouter
import supprimer
import modifier
import achat
import afficherAchat
#regex pour ussd
def mon_ussd(ussd):
    exprension = r'^\*(\d{1,3})#'
    if re.match(exprension,ussd) is not None:
        return('Ussd Valider.')
    else:
        return('Ooops....Regex non valider')



entre_regex = str(input("Composer votre USSD(: *150# :) :"))
if mon_ussd(entre_regex):
    print(mon_ussd(entre_regex))
    if entre_regex == '*150#':
        print('...........................'*3)
        mon_liste = ['kuraba ibidandazwa','Gushiramwo ikidandazwa','Guhanagura ikidandazwa',"Guhindura ibiranga ikidandazwa",'Kudandaza','kuraba ivyadandajwe','kuraba raporo']
        for numero, nListe in enumerate(mon_liste,start=1):
            print(f"{numero}.{nListe}")
        print(f"{0}.Guhagarika")
        while True:
            try:
                choixUssd = int(input("Shiramwo Igiharuro ca Menu :"))
                if choixUssd == 1:
                    afficher.afficher_donnees()
                elif choixUssd == 2:
                    ajouter.ajouter_donnees()
                elif choixUssd ==3:
                    supprimer.supprimer_donnees()
                elif choixUssd == 4:
                    modifier.modifier_donnees()
                elif choixUssd == 5:
                    achat.acheter_produit()
                elif choixUssd == 6:
                    afficherAchat.afficher_produits_vendus()
                elif choixUssd == 7:
                    print('Raba rapport mugasandungu kubutumwa rapport.txt. Murakoze')
                elif choixUssd == 0:
                    print("Kuvayo")
                    break
            except:
                print("Ibitigiri gusa nivyo vyemewe !. Murakoze")
        
        
    else:
        print("Mauvaise Ussd Veiller composer *150#")
else:
    print(mon_ussd(entre_regex))

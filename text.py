# from pprint import *
# data = {
#   "utilisateurs": [
#     {
#       "id": 1,
#       "nom": "Alice",
#       "age": 25,
#       "abonnement": True,
#       "notes": [5, 4, 3],
#       "tags": ["premium", "sport"]
#     },
#     {
#       "id": 2,
#       "nom": "Bob",
#       "age": 17,
#       "abonnement": False,
#       "notes": [2, 3],
#       "tags": ["gratuit", "musique"]
#     },
#     {
#       "id": 3,
#       "nom": "Charlie",
#       "age": 33,
#       "abonnement": True,
#       "notes": [4, 4, 5, 5],
#       "tags": ["premium", "cinéma"]
#     },
#     {
#       "id": 4,
#       "nom": "Diana",
#       "age": 70,
#       "abonnement": False,
#       "notes": [5],
#       "tags": ["gratuit", "sport", "santé"]
#     }
#   ]
# }

# donnee = data['utilisateurs']
# # pprint(donnee) exercice 1
# # for i in donnee:
# #     if i['abonnement']:
# #         print(i['nom'])
# # ma_som = []
# # for a in donnee:
# #     ff = a['notes']
# #     for i in ff:
# #         ma_som.append(i)
# #         somme+=i
    
#     # print(somme)




# class Project:
#     def __init__(self,rayon):
#         self.rayon = rayon
        

#     def diametre(self):
#         return self.rayon*2
    
#     def surface(self):
#         return 3.14*self.rayon**2
    
#     def __sub__(self,autre):
#         print(self.rayon - autre.rayon)
    
#     def __add__(self,autre):
#         print(self.rayon + autre.rayon)
            

# app = Project(4)

# print(app.diametre())
# print(app - Project(12))
# print(app + Project(23))


class Urukiramende:
    def __init__(self,l,L):
        self.l = l 
        self.L = L 
    
    def surface(self):
        return self.l * self.L
    

class Ikwadarato(Urukiramende):
    def __init__(self,c):
        pass
        

        



from random import randint 
import os
import time
from getpass import getpass

class  personnage(object):
    """
    Classe concrète, tu peux créer autant de pesonnage en jeu
    """
    def __init__(self): # constructeur
        self.ptsDeVie = 10
        self.positionX = 0
        self.positionY = -4

    def getPtsVie(self):
        return self.ptsDeVie

    def afficherPtsVie(self):
        print("Vous avez", self.ptsDeVie, "points de vie !")
        time.sleep(2)

    def movement(self, direction):
 
        if direction == 'Z': # vers le Nord
            if [self.positionX, self.positionY+1] in salle.getsurface():
                self.positionY+=1
            else:
                print("Vous allez dans le mur")
                time.sleep(1)

        elif direction == 'S': # vers le Sud
            if [self.positionX, self.positionY-1] in salle.getsurface():
                self.positionY-=1
            else:
                print("Vous allez dans le mur")
                time.sleep(1)

        elif direction == 'Q': # vers l'Ouest
            if [self.positionX-1, self.positionY] in salle.getsurface() or (self.positionX == -4 and self.positionY == 1):
                self.positionX-=1
            else:
                print("Vous allez dans le mur")
                time.sleep(1)

            if self.positionX == -5 and self.positionY == 1:
                print("""
_____________________¶ 
____________________¶_¶ 
____________________¶_¶ 
___________________¶__¶¶ 
___________________¶__¶¶ 
__________________¶____¶¶ 
_________________¶_____¶¶¶ 
_______________¶¶¶¶¶¶¶¶¶¶¶¶¶ 
________________¶_________¶ 
_____¶___________¶¶¶¶¶¶¶¶¶ 
_____¶____________¶_____¶ 
____¶_¶______¶____¶_____¶ 
____¶_¶______¶____¶_____¶ 
___¶__¶¶____¶_¶___¶_____¶ 
___¶__¶¶___¶__¶¶__¶_____¶________¶ 
__¶____¶¶_¶____¶¶_¶_____¶________¶ 
__¶____¶¶_¶¶¶¶¶¶¶_¶_____¶_______¶_¶ 
_¶_____¶¶¶¶¶___¶__¶_____¶_______¶_¶ 
_¶_____¶¶¶¶¶_¶_¶__¶_____¶______¶__¶¶ 
¶¶¶¶¶¶¶¶¶¶¶¶_¶_¶_¶¶¶¶¶¶¶¶¶_____¶__¶¶ 
_¶_______¶_¶_¶_¶¶_________¶___¶____¶¶ 
__¶¶¶¶¶¶¶__¶___¶¶_________¶_¶¶¶¶¶¶¶¶¶¶¶ 
___¶___¶___¶¶¶¶¶___________¶_¶_______¶ 
___¶___¶___¶___¶____________¶_¶¶¶¶¶¶¶¶ 
___¶_¶_¶__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶___¶__¶ 
___¶_¶_¶_¶___________________¶_¶_¶_¶_¶_¶ 
___¶___¶_¶__________________¶_¶_¶_¶¶___¶ 
___¶_¶_¶_¶___________________¶_¶___¶_¶¶¶ 
___¶_¶_¶_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶_¶_¶_¶_¶ 
___¶___¶___¶_____¶__¶_¶__¶_¶___¶_¶_¶_¶_¶ 
___¶___¶____¶___¶____¶____¶____¶___¶_¶_¶ 
___¶___¶_____¶__¶____¶___¶__¶¶¶¶¶¶¶¶¶¶¶¶ 
___¶___¶¶¶¶¶¶¶__¶____¶___¶¶¶¶¶¶¶¶______¶ 
___¶___¶_____¶__¶____¶___¶______¶_____¶ 
___¶___¶_____¶__¶____¶___¶_¶_¶_¶_¶____¶ 
___¶___¶_____¶__¶____¶___¶_______¶¶¶¶¶ 
¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶____¶___¶¶¶¶¶¶¶¶¶¶__¶ 
¶____________¶__¶____¶___¶_______¶___¶ 
¶¶¶¶¶¶¶¶¶¶¶¶¶¶__¶____¶___¶¶¶¶¶¶¶¶____¶ 
_¶__________¶¶__¶____¶___¶_____¶_¶_¶_¶ 
__¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶_¶_¶_¶ 
__¶________¶_________________¶_¶_____¶ 
__¶________¶_________________¶_¶_____¶ 
_¶¶¶_¶¶¶_¶¶¶_¶¶¶_________¶¶¶_¶¶¶_¶¶¶_¶¶¶ 
_¶_¶¶¶_¶¶¶_¶¶¶_¶¶¶¶¶¶¶¶¶¶¶_¶¶¶_¶¶¶_¶¶¶_¶ 
_¶_____________¶¶¶¶¶¶¶¶¶¶¶_____________¶ 
_¶_____________¶_________¶_____________¶ 
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_________¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶ 
_¶_____________________________________¶ 
__¶___________________________________¶ 
___¶¶¶¶¶¶¶¶¶¶¶_____¶¶¶_____¶¶¶¶¶¶¶¶¶¶¶ 
___¶_________¶____¶¶¶¶¶____¶_________¶ 
___¶_________¶___¶¶¶_¶¶¶___¶_________¶ 
___¶____¶____¶___¶¶___¶¶___¶____¶____¶ 
___¶___¶¶¶___¶__¶¶¶___¶¶¶__¶___¶¶¶___¶ 
___¶___¶¶¶___¶__¶¶_____¶¶__¶___¶¶¶___¶ 
___¶___¶¶¶___¶__¶¶_____¶¶__¶___¶¶¶___¶ 
___¶___¶¶¶___¶__¶¶_____¶¶__¶___¶¶¶___¶ 
¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶

BRAVO VOUS VOUS ÊTES ÉCHAPPÉ DU CHÂTEAU !
""")
                os._exit(0)

        elif direction == 'D': # vers l'Est
            if [self.positionX+1, self.positionY] in salle.getsurface():
                self.positionX+=1
            else:
                print("Vous allez dans le mur")
                time.sleep(1)
        
    def attaque(self):
        self.ptsDeVie-=2
        print("""
▒▒▒▒▒▒▒▒▄▄▄▄▄▄▄▄▒▒▒▒▒▒
▒▒█▒▒▒▄██████████▄▒▒▒▒
▒█▐▒▒▒████████████▒▒▒▒
▒▌▐▒▒██▄▀██████▀▄██▒▒▒
▐┼▐▒▒██▄▄▄▄██▄▄▄▄██▒▒▒
▐┼▐▒▒██████████████▒▒▒
▐▄▐████─▀▐▐▀█─█─▌▐██▄▒
▒▒█████──────────▐███▌
▒▒█▀▀██▄█─▄───▐─▄███▀▒
▒▒█▒▒███████▄██████▒▒▒
▒▒▒▒▒██████████████▒▒▒
▒▒▒▒▒█████████▐▌██▌▒▒▒
▒▒▒▒▒▐▀▐▒▌▀█▀▒▐▒█▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▌▒▒▒▒▒

ON VOUS ATTAQUE !
""")
        time.sleep(2)
    
    def fiole(self):
        if self.ptsDeVie <= 9:
            self.ptsDeVie+=1
            print("""
________██████_______________________
_____███████████____________███______
____█████████████_________██___██____
___███████████████______██~~~~~~~██__
___████████████████______██_°_°°██___
___████████████████_______██_°_██____
____███████████████________█████_____
_______███████████_______████________
___________███████______████_________
____________██████████████___________
__________██████████████_____________
_________████████████________________
_________████████████________________
________█████████████________________
________████████████_________________
_______█████████████_________________
_______██████████████________________
_______███████████████_______________
________███████████████______________
_______███████__████████_____________
______███████_____███████____________
____█████████________██████__________

VOUS AVEZ TROUVÉ UNE FIOLE !
""")
        else:
            print("""
—–-—▒▒▒▒▒▒▒▒▒▒
—–-▒███████████▒
—▒████▒▒▒▒▒▒▒███▒
-▒████▒▒▒▒▒▒▒▒▒███▒……………….▒▒▒▒▒▒
-▒███▒▒▒▒▒███▒▒▒███▒…………..▒██████▒
-▒███▒▒▒▒██████▒▒███▒……….▒██▒▒▒▒██▒
—▒███▒▒▒███████▒▒██▒…….▒███▒▒█▒▒██▒
—–▒███▒▒████████▒██▒…▒███▒▒███▒▒██▒
——–▒██▒▒██████████▒▒███▒▒████▒▒██▒
———▒██▒▒██████████████▒████▒▒██▒
———-▒██▒▒█████████████████▒▒██▒
————▒██▒▒██████████████▒▒██▒
————–▒██▒▒████████████▒▒██▒
—————-▒██▒▒██████████▒▒██▒
—————–▒██▒▒████████▒▒██▒
——————-▒██▒▒██████▒▒██▒
———————▒██▒▒████▒▒██▒
———————-▒██▒▒███▒▒█▒
————————▒██▒▒█▒▒█▒
————————-▒██▒▒▒█▒
—————————▒██▒█▒

VOUS AVEZ TROUVÉ UNE FIOLE MAIS VOUS ÊTES DÉJÀ EN PLEINE SANTÉ !
""")
        time.sleep(2)

    def localisation(self):
        print("Votre position : [", self.positionX, ",", self.positionY, "]")
        salle.which_room()
        time.sleep(2)
    

class salle(object):
    """
    Classe abstraite pour créer nos différentes salles
    """
    def __init__(self): # constructeur
        # Données communes à toutes les salles
        pass

    def which_room(self):
        pos = [perso.positionX, perso.positionY]
        searching = True

        while searching:
            room_finder = exterieur.getRoomPosition()
            if pos in room_finder:
                print("Vous êtes  à l'extérieur")
                searching = False
                break
            
            room_finder = cuisine.getRoomPosition()
            if pos in room_finder:
                print("Vous êtes  dans la cuisine")
                searching = False
                break

            room_finder = chambre.getRoomPosition()
            if pos in room_finder:
                print("Vous êtes  dans la chambre")
                searching = False
                break
            
            room_finder = salle_de_garde.getRoomPosition()
            if pos in room_finder:
                print("Vous êtes  dans la salle de garde")
                searching = False
                break

            room_finder = prison.getRoomPosition()
            if pos in room_finder:
                print("Vous êtes en prison")
                searching = False
                break

    # les classes concrètes (les différentes pièces ont accès)
    # méthode 
    def getRoomPosition(self):
        return self.room_position

    def getsurface(self):
        surface = exterieur.getRoomPosition() + cuisine.getRoomPosition() + chambre.getRoomPosition() + salle_de_garde.getRoomPosition() + prison.getRoomPosition()
        return surface
    
    def getmap(self):
        game_map = []
        for y in range(4, -5, -1):
            for x in range(-4, 5, 1):
                game_map.append([x, y])
        
        return game_map
    
    def afficher_map(self):
        game_map = salle.getmap()
        display = ""
        nine = 1
        for [x, y] in game_map: # foreach
            if [x, y] == [perso.positionX, perso.positionY]:
                display+="O"
            elif [x, y] in salle.getsurface(): # coutain
                display+="-"
            else:
                display+="X"
            if nine == 9:
                display+='\n'
                nine=1
            else:
                nine+=1

        print(display)

        
class exterieur(salle):
    # X : 2 à 4
    # Y : 1 à -1
    def __init__(self): # constructeur
        self.room_position = [
            [2, 1], [3, 1], [4, 1],
            [2, 0], [3, 0], [4, 0],
            [2, -1], [3, -1], [4, -1]
        ]

class cuisine(salle):
    # X : -2 à -4
    # Y : 1 à -1
    def __init__(self): # constructeur
        self.room_position = [
            [-4, 1], [-3, 1], [-2, 1],
            [-4, 0], [-3, 0], [-2, 0],
            [-4, -1], [-3, -1], [-2, -1]
        ]

class chambre(salle):
    def __init__(self): # constructeur
        # X : 1 à -1
        # Y : 2 à 4
        self.room_position = [
            [-1, 4], [0, 4], [1, 4],
            [-1, 3], [0, 3], [1, 3],
            [-1, 2], [0, 2], [1, 2]
        ]

class salleDeGarde(salle):
    # X : 1 à -1
    # Y : 1 à -1
    def __init__(self): # constructeur
        self.room_position = [
            [-1, 1], [0, 1], [1, 1],
            [-1, 0], [0, 0], [1, 0],
            [-1, -1], [0, -1], [1, -1]
        ]
        # portes [0, 1], [-1, 0], [1, 0], [0, -1]


class prison(salle):
    def __init__(self, room_name="prison"): # constructeur
        # X : 1 à -1
        # Y : -2 à -4
        self.room_position = [
            [-1, -2], [0, -2], [1, -2],
            [-1, -3], [0, -3], [1, -3],
            [-1, -4], [0, -4], [1, -4]
        ]            

if __name__ == "__main__":
    os.system('cls')
    # un seul personnage en jeu
    perso = personnage()

    # les pièces sont instanciés
    salle = salle()
    prison = prison()
    cuisine = cuisine()
    chambre = chambre()
    exterieur = exterieur()
    salle_de_garde = salleDeGarde()
    
    still_alive = True

    while still_alive:
        need_key = True
        while need_key:
            print("""
Pour vous déplacer, entrez la direction que vous désirez suivre (Z, Q, S, D)
Pour connaître votre position sur la carte , appuyez sur "M" 
Pour connaitre votre nombre de point de vie, appuyez sur "I"
""")
            salle.afficher_map()
            action = getpass("")
            # os.system('cls')

            if action.upper() == "I":
                perso.afficherPtsVie()

            elif action.upper() == "M":
                perso.localisation()

            elif action.upper() == "Z" or action.upper() == "Q" or action.upper() == "S" or action.upper() == "D":
                perso.movement(direction=action.upper())
                need_key = False

            os.system('cls')

        event = randint(1,3)
        if event==3:
            perso.fiole()
        elif event==2:
            perso.attaque()
            if perso.getPtsVie() <= 0:
                os.system('cls')
                print("""
´´´´´´´´´´´´´´´´´´´ ¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´´´´`
´´´´´´´´´´´´´´´´´¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´´
´´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´´
´´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´`´´´´´´´´´´´¶¶´´´´´´´´´´`
´´´´´´´´´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´¶¶´´´´´´´´´´
´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´´´´´
´´´´´´´´´´´¶¶´¶¶´´´¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´¶¶´¶¶´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶¶¶´´´´´´´´´´´
´´´´´´´´´´´´´¶¶¶´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶´¶¶¶´´´´´´´´´´´´´
´´´´¶¶¶´´´´´´´¶¶´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´¶¶´´´´´´¶¶¶¶´´´
´´´¶¶¶¶¶´´´´´¶¶´´´¶¶¶¶¶¶¶´´´¶¶¶´´´¶¶¶¶¶¶¶´´´¶¶´´´´´¶¶¶¶¶¶´´
´´¶¶´´´¶¶´´´´¶¶´´´´´¶¶¶´´´´¶¶¶¶¶´´´´¶¶¶´´´´´¶¶´´´´¶¶´´´¶¶´´
´¶¶¶´´´´¶¶¶¶´´¶¶´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´¶¶¶¶´´´´¶¶¶´
¶¶´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´¶¶
¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶´´´´¶¶¶¶¶¶¶¶´´´´´´¶¶¶¶¶¶¶¶
´´¶¶¶¶´¶¶¶¶¶´´´´´´¶¶¶¶¶´´´´´´´´´´´´´´¶¶¶´¶¶´´´´´¶¶¶¶¶¶´¶¶¶´
´´´´´´´´´´¶¶¶¶¶¶´´¶¶¶´´¶¶´´´´´´´´´´´¶¶´´¶¶¶´´¶¶¶¶¶¶´´´´´´´´
´´´´´´´´´´´´´´¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶¶¶¶¶¶´¶¶´¶¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´´´¶¶´¶¶´¶´¶´¶´¶´¶´¶´¶´¶´¶¶´´´´´´´´´´´´´´´´´
´´´´´´´´´´´´´´´´¶¶¶¶´´¶´¶´¶´¶´¶´¶´¶´¶´´´¶¶¶¶¶´´´´´´´´´´´´´´
´´´´´´´´´´´´¶¶¶¶¶´¶¶´´´¶¶¶¶¶¶¶¶¶¶¶¶¶´´´¶¶´¶¶¶¶¶´´´´´´´´´´´´
´´´´¶¶¶¶¶¶¶¶¶¶´´´´´¶¶´´´´´´´´´´´´´´´´´¶¶´´´´´´¶¶¶¶¶¶¶¶¶´´´´
´´´¶¶´´´´´´´´´´´¶¶¶¶¶¶¶´´´´´´´´´´´´´¶¶¶¶¶¶¶¶´´´´´´´´´´¶¶´´´
´´´´¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶´´´´´¶¶¶¶¶´´´´´¶¶¶´´´´
´´´´´´¶¶´´´¶¶¶´´´´´´´´´´´¶¶¶¶¶¶¶¶¶´´´´´´´´´´´¶¶¶´´´¶¶´´´´´´
´´´´´´¶¶´´¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶´´¶¶´´´´´´
´´´´´´´¶¶¶¶´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´¶¶¶¶´´´´´´´   

VOUS ÊTES MORT !
""")
                time.sleep(2)
                still_alive = False
                os._exit(0)

        os.system('cls')
